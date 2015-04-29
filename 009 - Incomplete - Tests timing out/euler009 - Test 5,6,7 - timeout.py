from math import sqrt

def get_py_triplets (N):

	result = -1

	for c in xrange(int(N/2 + 1)):
		for b in xrange(c):
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