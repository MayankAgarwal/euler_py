from math import sqrt

def get_primes (N):
	# [0,1,2,3,4,5.....]
	is_prime = [False, False] + [True]*N
	N = N+2
	primes = []

	for i in xrange(int(sqrt(N)) + 1):

		if not is_prime[i]:
			continue

		for j in xrange(i*i, N, i):
			is_prime[j] = False

	init_index = 0
	while True:
		try:
			init_index = is_prime.index(True, init_index)
			primes.append(init_index)
			init_index = init_index+1
		except ValueError:
			break

	return primes

def get_prime_factors_count (num, primes):

	prime_factor_count = 0
	total_factor_count = 1
	i = 0

	if num == 1:
		return 1

	for prime in primes:

		prime_factor_count = 0

		while num>1 and num%prime == 0:
			prime_factor_count += 1
			num = num/prime

		prime_factor_count += 1
		total_factor_count = total_factor_count*prime_factor_count

		if num<=1:
			break

	return total_factor_count

def get_triangle_number (N, primes):

	k = 0
	factor_count = -1

	while factor_count <= N:
		k += 1

		if k%2 == 0:
			c1 = get_prime_factors_count(k/2, primes)
			c2 = get_prime_factors_count(k+1, primes)
		else:
			c1 = get_prime_factors_count(k, primes)
			c2 = get_prime_factors_count((k+1)/2, primes)

		factor_count = c1 * c2

	num = k*(k+1)/2
	return num

tests = int(raw_input())
primes = get_primes(500)

for test in xrange(tests):
	N = int(raw_input())
	print get_triangle_number(N, primes)