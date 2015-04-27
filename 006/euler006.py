def get_series_difference (n):

	square_series_sum = (n*(n+1)*(2*n+1))/6
	linear_seies_sum = n*(n+1)/2

	answer = (linear_seies_sum)**2 - square_series_sum

	return answer


tests = int(raw_input())

for test in xrange(tests):

	N = int(raw_input())

	print get_series_difference(N)