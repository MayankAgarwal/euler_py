from math import sqrt

def get_triangle_number(N):

	k = 1

	while True:

		num = k*(k+1)/2
		factor_count = 0

		for i in xrange(1, int(sqrt(num))+1):

			if num==1:
				factor_count += 1
			elif num%i == 0:
				factor_count += 2

		print num, factor_count

		if factor_count > N:
			return num

		k += 1


tests = int(raw_input())

for test in xrange(tests):

	N = int(raw_input())

	if N == 1:
		print 3

	print get_triangle_number(N)