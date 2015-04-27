tests = int(raw_input().strip())

for test in xrange(tests):

    N = int(raw_input().strip())

    a = 2

    # 
    # Loop until sqrt(N) rather than N.
    # Ex: N = 22 ==> 2 x 11, Loop until sqrt(22) = 4 and then divide revursively over all factors. If in the end, N is equal to 1
    # All factors have been found. Else the remaining number is largest prime factor
    # 
    while a*a <= N:

        if N%a == 0:
            N = N/a
        else:
            a += 1

    if N != 1:
    	a=N

    print a