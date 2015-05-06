from math import sqrt

def get_divisor_sum (num):

	sum = 1

	for i in xrange(2, int(sqrt(num)) + 1):

		if num%i == 0:
			sum += i

			if i*i != num:
				sum += (num/i)

	return sum


def precompute_amicable_numbers(N):

	amicable_numbers = []

	for i in xrange(N+1):

		temp = get_divisor_sum(i)

		# sum of divisors == original number. Ex: 6 = 1+2+3
		if temp == i:
			continue

		if get_divisor_sum(temp) == i:
			amicable_numbers.append(temp)
			amicable_numbers.append(i)

	return set(amicable_numbers)


__MAX_N = 10**5
amicable_numbers = precompute_amicable_numbers(__MAX_N)

tests = int(raw_input())

for test in xrange(tests):
	N = int(raw_input())
	print sum(filter(lambda x: x<N, amicable_numbers))