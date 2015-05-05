from math import sqrt, log10, ceil

# Brute-force method
# Takes around 17 seconds for N = 5000
def get_min_fibo(digit_length):

    a,b = 0,1
    c = a+b
    i = 2

    while len(str(c)) < digit_length:
        a,b = b,c
        c = a+b
        i += 1

    return i

# Estimation of sequence index
# Refer http://www.mathblog.dk/project-euler-25-fibonacci-sequence-1000-digits/
# for the formula
def get_min_fibo_est(digit_length):

    phi = (1+sqrt(5))/2

    num = (digit_length-1) + log10(5)/2
    den = log10(phi)

    n = ceil(num/den)

    return int(n)


tests = int(raw_input())

for test in xrange(tests):
    N = int(raw_input())
    print get_min_fibo_est(N)