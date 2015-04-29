def get_py_triplets(N):

	result = -1

	for c in xrange(int(N/3), int(N/2)):

		abc = (c*N*N - 2*c*c*N)/2

		print c, abc

		if abc == int(abc) and abc>result:
			result = abc

	return result


tests = int(raw_input())

for test in xrange(tests):
	N = int(raw_input())

	print get_py_triplets(N)