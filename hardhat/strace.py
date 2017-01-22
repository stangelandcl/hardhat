import os
import platform
import re
import subprocess
import tempfile
from .util import Object


def normalize_path(path):
    return os.path.normcase(os.path.abspath(path))  # Windows requires normcase


_possible_system_calls = [
    'open',
    'openat',
    'stat',
    'stat64',
    'lstat',
    'lstat64',
    'read',
    'write',
    'newfstatat',
    'newfstatat64',
    'fstatat',
    'fstatat64',
    'execve',
    'exit_group',
    'chdir',
    'mkdir',
    'rename',
    'clone',
    'vfork',
    'fork',
    'symlink',
    'creat',
]


def get_strace_system_calls():
    """ Return None if this system doesn't have strace, otherwise
    return a comma seperated list of system calls supported by strace. """
    if platform.system() == 'Windows':
        # even if windows has strace, it's probably a dodgy cygwin one
        return None

    valid_system_calls = []
    try:
        # check strace is installed and if it supports each type of call
        for system_call in _possible_system_calls:
            proc = subprocess.Popen(
                ['strace', '-e', 'trace=' + system_call],
                stderr=subprocess.PIPE)
            stdout, stderr = proc.communicate()
            proc.wait()

            stderr = stderr.decode()
            if 'invalid system call' not in stderr:
                valid_system_calls.append(system_call)
    except OSError:
        return None
    return ','.join(valid_system_calls)


class StraceProcess(Object):
    def __init__(self, cwd='.', delayed=False):
        self.cwd = cwd
        self.deps = set()
        self.outputs = set()
        self.delayed = delayed
        self.delayed_lines = []

    def add_dep(self, dep):
        self.deps.add(dep)

    def add_output(self, output):
        self.outputs.add(output)

    def add_delayed_line(self, line):
        self.delayed_lines.append(line)

    def __str__(self):
        return '<StraceProcess cwd=%s deps=%s outputs=%s>' % \
               (self.cwd, self.deps, self.outputs)


class StraceRunner(Runner):
    keep_temps = False

    def __init__(self, builder, build_dir=None):
        self.strace_system_calls = StraceRunner.get_strace_system_calls()
        if self.strace_system_calls is None:
            raise Exception('strace is not available')
        self._builder = builder
        self.temp_count = 0
        self.build_dir = normalize_path(build_dir or os.getcwd())

    # Regular expressions for parsing of strace log
    _open_re       = re.compile(r'(?P<pid>\d+)\s+open\("(?P<name>[^"]*)", (?P<mode>[^,)]*)')
    _openat_re     = re.compile(r'(?P<pid>\d+)\s+openat\(AT_FDCWD, "(?P<name>[^"]*)", (?P<mode>[^,)]*)')
    _stat_re       = re.compile(r'(?P<pid>\d+)\s+l?stat(?:64)?\("(?P<name>[^"]*)", .*') # stat,lstat,stat64,lstat64
    _statat_re     = re.compile(r'(?P<pid>\d+)\s+(new)?fstatat(?:64)?\(AT_FDCWD, "(?P<name>[^"]*)", .*') # newfstatat,newfstatat64,fstatat,fstatat64
    _execve_re     = re.compile(r'(?P<pid>\d+)\s+execve\("(?P<name>[^"]*)", \[(?P<cmd>[^]]*)\].*= 0$')
    _creat_re      = re.compile(r'(?P<pid>\d+)\s+creat\("(?P<name>[^"]*)", .*')
    _mkdir_re      = re.compile(r'(?P<pid>\d+)\s+mkdir\("(?P<name>[^"]*)", .*\)\s*=\s(?P<result>-?[0-9]*).*')
    _rename_re     = re.compile(r'(?P<pid>\d+)\s+rename\("[^"]*", "(?P<name>[^"]*)"\)')
    _symlink_re    = re.compile(r'(?P<pid>\d+)\s+symlink\("[^"]*", "(?P<name>[^"]*)"\)')
    _kill_re       = re.compile(r'(?P<pid>\d+)\s+killed by.*')
    _chdir_re      = re.compile(r'(?P<pid>\d+)\s+chdir\("(?P<cwd>[^"]*)"\)')
    _exit_group_re = re.compile(r'(?P<pid>\d+)\s+exit_group\((?P<status>.*)\).*')
    _clone_re      = re.compile(r'(?P<pid_clone>\d+)\s+(clone|fork|vfork)\(.*\)\s*=\s*(?P<pid>\d*)')
    _read_re       = re.compile(r'(?P<pid>\d+)\s+read\("(?P<name>[^"]*)", .*')
    _readfd_re     = re.compile(r'(?P<pid>\d+)\s+read\((?P<fd>\d+)<(?P<name>[^>]*)>, .*')
    _write_re      = re.compile(r'(?P<pid>\d+)\s+write\("(?P<name>[^"]*)", .*')
    _writefd_re    = re.compile(r'(?P<pid>\d+)\s+write\((?P<fd>\d+)<(?P<name>[^>]*)>, .*')


    # Regular expressions for detecting interrupted lines in strace log
    # 3618  clone( <unfinished ...>
    # 3618  <... clone resumed> child_stack=0, flags=CLONE, child_tidptr=0x7f83deffa780) = 3622
    _unfinished_start_re = re.compile(r'(?P<pid>\d+)(?P<body>.*)<unfinished ...>$')
    _unfinished_end_re   = re.compile(r'(?P<pid>\d+)\s+\<\.\.\..*\>(?P<body>.*)')

    def _do_strace(self, args, kwargs, outfile, outname):
        """ Run strace on given command args/kwargs, sending output to file.
            Return (status code, list of dependencies, list of outputs). """
        shell_keywords = dict(silent=False)
        shell_keywords.update(kwargs)
        try:
            fabricate.shell('strace', '-fo', outname, '-e',
                  'trace=' + self.strace_system_calls,
                  args, **shell_keywords)
        except ExecutionError as e:
            # if strace failed to run, re-throw the exception
            # we can tell this happend if the file is empty
            outfile.seek(0, os.SEEK_END)
            if outfile.tell() is 0:
                raise e
            else:
                # reset the file postion for reading
                outfile.seek(0)

        self.status = 0
        processes  = {}  # dictionary of processes (key = pid)
        unfinished = {}  # list of interrupted entries in strace log
        for line in outfile:
           self._match_line(line, processes, unfinished)

        # collect outputs and dependencies from all processes
        deps = set()
        outputs = set()
        for pid, process in processes.items():
            deps = deps.union(process.deps)
            outputs = outputs.union(process.outputs)

        return self.status, list(deps), list(outputs)

    def _match_line(self, line, processes, unfinished):
        # look for split lines
        unfinished_start_match = self._unfinished_start_re.match(line)
        unfinished_end_match = self._unfinished_end_re.match(line)
        if unfinished_start_match:
            pid = unfinished_start_match.group('pid')
            body = unfinished_start_match.group('body')
            unfinished[pid] = pid + ' ' + body
            return
        elif unfinished_end_match:
            pid = unfinished_end_match.group('pid')
            body = unfinished_end_match.group('body')
            line = unfinished[pid] + body
            del unfinished[pid]

        is_output = False
        open_match = self._open_re.match(line)
        openat_match = self._openat_re.match(line)
        stat_match = self._stat_re.match(line)
        statat_match = self._statat_re.match(line)
        execve_match = self._execve_re.match(line)
        creat_match = self._creat_re.match(line)
        mkdir_match = self._mkdir_re.match(line)
        symlink_match = self._symlink_re.match(line)
        rename_match = self._rename_re.match(line)
        clone_match = self._clone_re.match(line)
        read_match = self._read_re.match(line)
        readfd_match = self._readfd_re.match(line)
        write_match = self._write_re.match(line)
        writefd_match = self._writefd_re.match(line)

        kill_match = self._kill_re.match(line)
        if kill_match:
            return None, None, None

        match = None
        if execve_match:
            pid = execve_match.group('pid')
            match = execve_match # Executables can be dependencies
            if pid not in processes and len(processes) == 0:
                # This is the first process so create dict entry
                processes[pid] = StraceProcess()
        elif clone_match:
            pid = clone_match.group('pid')
            pid_clone = clone_match.group('pid_clone')
            if pid not in processes:
                # Simple case where there are no delayed lines
                processes[pid] = StraceProcess(processes[pid_clone].cwd)
            else:
                # Some line processing was delayed due to an interupted clone_match
                processes[pid].cwd = processes[pid_clone].cwd # Set the correct cwd
                processes[pid].delayed = False # Set that matching is no longer delayed
                for delayed_line in processes[pid].delayed_lines:
                    # Process all the delayed lines
                    self._match_line(delayed_line, processes, unfinished)
                processes[pid].delayed_lines = [] # Clear the lines
        elif open_match:
            match = open_match
            mode = match.group('mode')
            if 'O_WRONLY' in mode or 'O_RDWR' in mode:
                # it's an output file if opened for writing
                is_output = True
        elif openat_match:
            match = openat_match
            mode = match.group('mode')
            if 'O_WRONLY' in mode or 'O_RDWR' in mode:
                # it's an output file if opened for writing
                is_output = True
        elif read_match:
            match = read_match
        elif readfd_match:
            fd = int(readfd_match.group('fd'))

            # we don't want any process which reads from stdin
            if fd == 0:
                pid  = readfd_match.group('pid')
                if pid in processes:
                    processes[pid].readstdin = True
            else:
                match = readfd_match
        elif write_match:
            match = write_match
        elif writefd_match:
            fd = int(writefd_match.group('fd'))

            # we don't want any process which writes to stdout or stderr
            if fd == 1 or fd == 2:
                pid  = writefd_match.group('pid')
                if pid in processes:
                    processes[pid].writestdout = True
            else:
                match = writefd_match
        elif stat_match:
            match = stat_match
        elif statat_match:
            match = statat_match
        elif creat_match:
            match = creat_match
            # a created file is an output file
            is_output = True
        elif mkdir_match:
            match = mkdir_match
            if match.group('result') == '0':
                # a created directory is an output file
                is_output = True
        elif symlink_match:
            match =  symlink_match
            # the created symlink is an output file
            is_output = True
        elif rename_match:
            match = rename_match
            # the destination of a rename is an output file
            is_output = True

        if match:
            name = match.group('name')
            pid  = match.group('pid')
            if not self._matching_is_delayed(processes, pid, line):
                cwd = processes[pid].cwd
                if cwd != '.':
                    name = os.path.join(cwd, name)

                # normalise path name to ensure files are only listed once
                name = os.path.normpath(name)

                # if it's an absolute path name under the build directory,
                # make it relative to build_dir before saving to .deps file
                if os.path.isabs(name) and name.startswith(self.build_dir):
                    name = name[len(self.build_dir):]
                    name = name.lstrip(os.path.sep)

                if (self._builder._is_relevant(name)
                    and not self.ignore(name)
                    and os.path.lexists(name)):
                    if is_output:
                        processes[pid].add_output(name)
                    else:
                        processes[pid].add_dep(name)

        match = self._chdir_re.match(line)
        if match:
            pid  = match.group('pid')
            if not self._matching_is_delayed(processes, pid, line):
                processes[pid].cwd = os.path.join(processes[pid].cwd, match.group('cwd'))

        match = self._exit_group_re.match(line)
        if match:
            self.status = int(match.group('status'))

    def _matching_is_delayed(self, processes, pid, line):
        # Check if matching is delayed and cache a delayed line
        if pid not in processes:
             processes[pid] = StraceProcess(delayed=True)

        process = processes[pid]
        if process.delayed:
            process.add_delayed_line(line)
            return True
        else:
            return False

    def __call__(self, *args, **kwargs):
        """ Run command and return its dependencies and outputs, using strace
            to determine dependencies (by looking at what files are opened or
            modified). """
        if not self.quiet:
            echocmd(args, kwargs)
        ignore_status = kwargs.pop('ignore_status', False)
        if self.keep_temps:
            outname = 'strace%03d.txt' % self.temp_count
            self.temp_count += 1
            handle = os.open(outname, os.O_CREAT)
        else:
            handle, outname = tempfile.mkstemp()

        try:
            try:
                outfile = os.fdopen(handle, 'r')
            except:
                os.close(handle)
                raise
            try:
                status, deps, outputs = self._do_strace(args, kwargs, outfile, outname)
                if status is None:
                    raise Exception(
                        '%r was killed unexpectedly' % args[0], '', -1)
            finally:
                outfile.close()
        finally:
            if not self.keep_temps:
                os.remove(outname)

        if status and not ignore_status:
            print('args[0]=',args[0])
            raise ExecutionError('%s exited with status %d'
                                 % (' '.join(args[0]), status),
                                 '', status)
        return list(deps), list(outputs)
