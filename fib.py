import time
import cyfib
import cyfib_static



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







foo = 39

print("######Cython#########\n")

t0 = time.time()
print(cyfib.fib_rec(foo))
t1 = time.time()
print(cyfib.fib_rec2(foo))
t2 = time.time()
print(cyfib.fib_it(foo))
t3 = time.time()
print('recursive: {}\nrecursive2: {}\niterative: {}'.format(t1-t0, t2-t1, t3-t2))


print("######Static Cython#########\n")

t0 = time.time()
print(cyfib_static.fib_rec(foo))
t1 = time.time()
print(cyfib_static.fib_rec2(foo))
t2 = time.time()
print(cyfib_static.fib_it(foo))
t3 = time.time()
print('recursive: {}\nrecursive2: {}\niterative: {}'.format(t1-t0, t2-t1, t3-t2))

print("######Pure Python#########\n")

t0 = time.time()
print(fib_rec(foo))
t1 = time.time()
print(fib_rec2(foo))
t2 = time.time()
print(fib_it(foo))
t3 = time.time()
print('recursive: {}\nrecursive2: {}\niterative: {}'.format(t1-t0, t2-t1, t3-t2))