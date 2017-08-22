import os
import shutil
from .base import GnuRecipe


class LaceRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LaceRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '45e546e306c73ceed68329189f8f75fe' \
                      'cee3a1db8abb02b5838674a98983c5fe'
        self.name = 'lace'
        self.version = '0d882b10129789cacf901606b972e3159b8ae9b0'
        self.depends = ['hwloc']
        self.url = self.github_commit('trolando')
        self.configure_args = [
            'cmake',
            '-G',
            '"Unix Makefiles"',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            '..']

    def configure(self):
        dir = os.path.join(self.directory, 'build')
        os.makedirs(dir)
        old = self.directory
        self.directory = dir
        super(LaceRecipe, self).configure()


    def install(self):
        super(LaceRecipe, self).install()
        text = r'''
Lace

Lace is a C library that implements work-stealing. Work-stealing is a method for load balancing task-based parallel programs.

Lace is developed (2012-2014) by the Formal Methods and Tools group at the University of Twente. It is licensed with the Apache 2.0 license.

Download

You can clone our Git repository: http://fmt.ewi.utwente.nl/tools/scm/lace.git.

Alternatively, you can download a recent snapshot.

Please let us know if you use Lace in your project.

Testing / Benchmarking

To compile and run the test benchmarks, you need CMake and Python. In a terminal/command line, run the following commands:

cmake .
make
python bench.py
The benchmark script automatically detects the number of CPUs on your system and runs the benchmarks fib, uts, matmul and queens.

Usage

To use Lace in your own projects, you need to generate the header file lace.h. Use the following command to generate this file, replacing N by the highest number of parameters in your tasks:

lace.sh N > lace.h
For example, with N=3, lace.h defines macros TASK_1, TASK_2 and TASK_3 for tasks with 1, 2 or 3 parameters.

Include lace.h when defining tasks. Add lace.c to the source files of your program.

You can separate declaration and implementation using TASK_DECL_* and TASK_IMPL_*. For tasks that don't return a value, use VOID_TASK_*.

For example, to parallelize void search(int a, int b):

// search.h
#include <lace.h>
VOID_TASK_DECL_2(search, int, int);
#define search(a, b) CALL(search, (a), (b))

// search.c
#include <search.h>
VOID_TASK_IMPL_2(search, int, a, int, b)
{
    // Implementation here...
}

// some_file.c
#include <search.h>
void some_function()
{
    // ...
    search(a, b); // execute search in parallel
    // alternatively use: CALL(search, a, b);
    // ...
}
If you run your program on a NUMA system, set preprocessor define USE_NUMA=1 and add numa_tools.c to the source files of your program.

When using Lace, you need to tell it how many workers there are with a call to lace_init. This function takes two parameters: the number of workers and the (static) size of the task queue of each worker. This initializes Lace, but does not start the worker threads. For the size of the task queue you can use some high number, e.g. 1,000,000. The memory is virtually allocated using mmap but not actually allocated by the kernel until it is used, so a large size is no problem in current multi-core systems.

You can then start the worker pthreads using lace_startup. This function takes three parameters: the size of the program stack of the new pthreads, a Lace callback task that is the starting point of the parallel program, and a parameter for that task. If the first parameter is set to 0, then the default behavior is to allocate a program stack of the same size as the calling thread. If the second and third parameter are set, then the calling thread is suspended until the supplied Lace task is completed and the Lace framework is automatically shut down. If the second and third parameter are set to NULL, then Lace returns control to the calling thread, which is initialized as a Lace worker thread. The function lace_exit must be called manually to shutdown Lace afterwards.

For example:

// fib.h
#include <lace.h>
TASK_DECL_1(int, fib, int);
#define fib(n) CALL(fib, (n))

// fib.c
#include <fib.h>
TASK_IMPL_1(int, fib, int, n)
{
    if (n<2) return n;
    SPAWN(fib, n-1);
    SPAWN(fib, n-2);
    int fib_minus_2 = SYNC(fib);
    // Alternatively, instead of SPAWN/SYNC, use:
    // int fib_minus_2 = CALL(fib, n-2);
    int fib_minus_1 = SYNC(fib);
    return fib_minus_1 + fib_minus_2;
}

// main.c
#include <fib.h>

LACE_CALLBACK(startup)
{
    int n = (int)arg;
    printf("fib(%d) = %d\n", n, fib(n));
}

int main(int argc, char** argv) {
    int n = 40;

    // Initialize for 4 workers and some large enough deque size
    lace_init(4, 1000000);

    // Launch 3 workers plus 1 worker starting in 'startup' and suspend caller...
    lace_startup(0, startup, (void*)n);

    // Alternative: launch 3 workers, and return to caller...
    lace_startup(0, NULL, NULL);
    printf("fib(%d) = %d\n", n, fib(n));
    lace_exit();

    return 0;
}
It is also possible to manually start worker threads and use lace_init_worker to initialize each worker, then use lace_steal_loop to participate in work-stealing until Lace is shutdown. Note that there is a barrier in Lace initialization code that waits until all workers are initialized, and a barrier in the shutdown code that waits until all workers return.
'''
        doc_dir = os.path.join(self.prefix_dir, 'share', 'doc', 'lace')
        if os.path.exists(doc_dir):
            shutil.rmtree(doc_dir)

        os.makedirs(doc_dir)
        doc_file = os.path.join(doc_dir, 'README')
        self.log_dir('install', doc_dir, 'README documentation')
        with open(doc_file, 'wt') as f:
            f.write(text)
