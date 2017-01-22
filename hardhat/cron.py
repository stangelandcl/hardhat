import os
import tempfile
import uuid
from hardhat.util import open_file, run_or_error


class Cron:
    def __init__(self, environment):
        self.env = environment
        self.tmp_dir = tempfile.gettempdir()
        self.tmp_file = str(uuid.uuid4())[:8]
        self.tmp = os.path.join(self.tmp_dir, self.tmp_file)

    def read(self):
        cmd = ['crontab', '-l']
        cron = run_or_error(cmd, self.tmp_dir, self.env)
        return cron.split('\n')

    def write(self, cronl):
        cron = '\n'.join(cronl)

        #    print('import cron file %s:\n%s' % (tmp, cron))
        with open_file(self.tmp, 'wt', encoding='utf-8') as f:
            f.write(cron)
            f.write('\n')

        args = ['crontab', self.tmp]
        run_or_error(args, self.tmp_dir, self.env)

        os.remove(self.tmp)


def fullname(name):
    return '# HARDHAT_CRONJOB: ' + name


def remove_job(cronl, name):
    name = fullname(name)
    try:
        i = cronl.index(name)
        del cronl[i]  # name comment
        del cronl[i]  # job
    except ValueError:
        pass
    while len(cronl) and not cronl[-1].strip():
        del cronl[-1]


def delete_cron_job(name, env):
    cron = Cron(env)
    cronl = cron.read()
    remove_job(cronl, name)
    cron.write(cronl)


def add_cron_job(name, job, env):
    cron = Cron(env)
    cronl = cron.read()
    remove_job(cronl, name)
    cronl.append(fullname(name))
    cronl.append(job)
    cron.write(cronl)

##Ansible: dnsupdater
#0 * * * * /home/stangecl/updatedns.py
#Ansible: update launch data
#0 5 * * * /home/stangecl/data/update.sh
#Ansible: guix_823dced6562c
#@reboot /home/stangecl/guix/823dced6562c/bin/guix-daemon --disable-chroot --no-substitutes > /home/stangecl/guix/823dced6562c/var/log/guix-daemon.log 2>&1


if __name__ == '__main__':
    x = add_cron_job(
        'system_activity_update',
        '*/10 * * * * /home/stangecl/hardhat/20160630/usr/lib64/sa/sa1 1 1', {})
    print(x)
