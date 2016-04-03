import time

import cyfib
import cyfib_static
import ext_fib


def fib_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)

def fib_rec2(n):
    if n == 0:
        return (0,0)
    elif n == 1:
        return (0,1)
    else:
        (first, second) = fib_rec2(n-1)
        return (second, first + second)

def fib_it(n):
    first, second = 0, 1
    for i in range(n):
        first, second = second, first + second
    return first


def pure_python(n):
    print("\n######Pure Python#########\n")
    t0 = time.time()
    fib_rec(n)
    t1 = time.time()
    fib_rec2(n)
    t2 = time.time()
    fib_it(n)
    t3 = time.time()
    print('recursive: {}\nrecursive2: {}\niterative: {}'.format(t1 - t0, t2 - t1, t3 - t2))


def pure_cython(n):
    print("\n######Cython#########\n")
    t0 = time.time()
    cyfib.fib_rec(n)
    t1 = time.time()
    cyfib.fib_rec2(n)
    t2 = time.time()
    cyfib.fib_it(n)
    t3 = time.time()
    print('recursive: {}\nrecursive2: {}\niterative: {}'.format(t1 - t0, t2 - t1, t3 - t2))


def static_cython(n):
    print("\n######Static Cython#########\n")
    t0 = time.time()
    cyfib_static.fib_rec(n)
    t1 = time.time()
    cyfib_static.fib_rec2(n)
    t2 = time.time()
    cyfib_static.fib_it(n)
    t3 = time.time()
    print('recursive: {}\nrecursive2: {}\niterative: {}'.format(t1 - t0, t2 - t1, t3 - t2))


def c_api(n):
    print("\n######C-API Python#########\n")
    t0 = time.time()
    ext_fib.fib_rec(n)
    t1 = time.time()
    ext_fib.fib_it(n)
    t3 = time.time()
    print('recursive: {}\niterative: {}'.format(t1 - t0, t3 - t1))


foo = 45

pure_python(foo)
pure_cython(foo)
static_cython(foo)
c_api(foo)
