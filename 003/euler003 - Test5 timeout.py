tests = int(raw_input().strip())

for test in xrange(tests):

    N = int(raw_input().strip())

    a = 2

    while N != 1:

        if N%a == 0:
            N = N/a
        else:
            a += 1

    print a