# Execution time reduced for test cases. Test case 4 time reduced from ~9seconds to ~3 seconds.
# Still the programs times out for tests 5,6,and 7

from math import sqrt

def get_py_triplets (N):

	result = -1

	for c in xrange(int(N/3), int(N/2)):
		for b in xrange(int( (N-c)/2 ), c):
			a = N - b - c

			if a >= b:
				continue

			if (a*a + b*b) == c*c:
				temp = a*b*c

				if temp > result:
					result = temp

	return result


tests = int(raw_input())

for test in xrange(tests):
	N = int(raw_input())

	print get_py_triplets(N)