#cython
def fib_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)

def fib_rec2( n):
    if n == 0:
        return (0, 0)
    elif n == 1:
        return (0, 1)
    else:
        (first, second) = fib_rec2(n-1)
        return (second, first + second)

def fib_it( n):
    first, second = 0, 1
    for i in range(n):
        first, second = second, first + second
    return first

#static cython

def fib_rec_static(int n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec_static(n - 1) + fib_rec_static(n - 2)

def fib_rec2_static(int n):
    cdef int first, second
    if n == 0:
        return (0, 0)
    elif n == 1:
        return (0, 1)
    else:
        (first, second) = fib_rec2_static(n - 1)
        return (second, first + second)

def fib_it_static(int n):
    cdef int first, second
    first, second = 0, 1
    for i in range(n):
        first, second = second, first + second
    return first

######################
#cdef cython
######################

def fib_rec_cdef(n):
    return fib_rec_c(n)

def fib_rec2_cdef(n):
    return fib_rec2_c(n)

def fib_it_cdef(n):
    return fib_it_c(n)

cdef int fib_rec_c(int n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec_c(n - 1) + fib_rec_c(n - 2)

cdef fib_rec2_c(int n):
    cdef int first, second
    if n == 0:
        return (0, 0)
    elif n == 1:
        return (0, 1)
    else:
        (first, second) = fib_rec2_c(n - 1)
        return (second, first + second)

cdef int fib_it_c(int n):
    cdef int first, second
    first, second = 0, 1
    for i in range(n):
        first, second = second, first + second
    return first

######################
#cpdef cython
######################

cpdef fib_rec_cpdef(int n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec_cpdef(n - 1) + fib_rec_cpdef(n - 2)

cpdef fib_rec2_cpdef(int n):
    cdef int first, second
    if n == 0:
        return (0, 0)
    elif n == 1:
        return (0, 1)
    else:
        (first, second) = fib_rec2_cpdef(n - 1)
        return (second, first + second)

cpdef int fib_it_cpdef(int n):
    cdef int first, second
    first, second = 0, 1
    for i in range(n):
        first, second = second, first + second
    return first
