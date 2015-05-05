'''
Not an efficient solution. Takes 9.34 seconds for Test #3. Still within limits
'''

from math import sqrt

def get_divisor_sum(N):

	sum = 1 # 1 divides every number thus sum is 1

	if N == 1:
		return 1
	if N == 0:
		return 0
	
	for i in xrange(2, int(sqrt(N)) + 1):
		if N%i == 0:
			sum += i
			
			# escape perfect square condition
			if i*i != N:
				sum += (N/i)

	return sum


def init_abundant_numbers(MAX_LIMIT):

	abundant_numbers = []

	for i in xrange(1, MAX_LIMIT+1):

		if get_divisor_sum(i) > i:
			abundant_numbers.append(i)

	return abundant_numbers


def is_abundant_sum_possible(abundant_numbers, N):

	i = 0

	while abundant_numbers[i] < N:
		if (N - abundant_numbers[i]) in abundant_numbers:
			return "YES"
		i += 1

	return "NO"


MAX = 10**5
abundant_numbers = init_abundant_numbers(MAX)

tests = int(raw_input())

for test in xrange(tests):
	N = int(raw_input())
	print is_abundant_sum_possible(abundant_numbers, N)