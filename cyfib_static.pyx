
def fib_rec(int n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)

def fib_rec2(int n):
    cdef int first, second
    if n == 0:
        return (0, 0)
    elif n == 1:
        return (0, 1)
    else:
        (first, second) = fib_rec2(n-1)
        return (second, first + second)

def fib_it(int n):
    cdef int first, second
    first, second = 0, 1
    for i in range(n):
        first, second = second, first + second
    return first





