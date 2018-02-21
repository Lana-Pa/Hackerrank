def fib(n):
    if n < 0:
        raise ValueError ("N is negative")
    if n in (0,1):
        print n
    x1 = 0
    x2 = 1
    print x2

    for i in xrange(n-1):

        fib = x1+x2
        x1 = x2
        x2 = fib
        print fib
fib(5)


