# Not really an optimized solution but passes the time limit applied by HackerRank (10 seconds)
# 1 <= T <= 10^4
# 1 <= N <= 10^6
# Minimum test execution time: 6.5 seconds
# Maximum test execution time: 6.69 seconds
# 
# Submission URL: https://www.hackerrank.com/contests/projecteuler/challenges/euler010/submissions/code/3159795
# 

from itertools import count, islice
from math import sqrt

def init_primes():

	N = 10**6
	primes = []
	cumulative_sum = [0]

	for i in xrange(2, N):

		if all(i%j for j in islice(count(2), int(sqrt(i))-1)):
			primes.append(i)
			cumulative_sum.append(cumulative_sum[-1] + i)

	return primes, cumulative_sum


def binary_search(arr, num):

	low = 0;
	high = len(arr)-1
	mid = int((low+high)/2)

	while low<=mid<=high:

		if arr[mid] == num:
			return mid
		elif arr[mid-1] < num < arr[mid]:
			return mid-1

		if arr[mid] > num:
			high = mid-1
		elif arr[mid] < num:
			low = mid + 1

		mid = int((low+high)/2)

	return len(arr)-1

precomputed_primes, precomputed_cum_sum = init_primes()

tests = int(raw_input())

for test in xrange(tests):
	N = int(raw_input())

	index = binary_search(precomputed_primes, N)
	print precomputed_cum_sum[index+1]