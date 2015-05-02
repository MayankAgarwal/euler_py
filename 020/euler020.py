from math import log10, ceil

def precompute_N_factorial(length=1000):

	factorial = [1]*(length+1)

	for i in xrange(1, length+1):
		
		if i%10 == 0:
			factorial[i] = factorial[i-1]

		temp = factorial[i-1] * i

		while temp%10 == 0:
			temp = temp/10

		factorial[i] = temp

	return factorial



def get_digit_sum(num):
	num_digits = map(int, list(str(num)))
	return sum(num_digits)


factorial = precompute_N_factorial()

tests = int(raw_input())

for test in xrange(tests):
	N = int(raw_input())
	print get_digit_sum(factorial[N])