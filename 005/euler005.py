# Usage: GCD (6,4), or GCD(100, 6)
def GCD (a,b):

	if a%b == 0:
		return b

	return GCD(b, a%b)

def LCM (a,b):
	return (a/GCD(a, b)) * b


def get_smallest_number(N):

	result = 1

	for i in xrange(1, N+1):
		result = LCM(result, i)

	return result


tests = int(raw_input())

for test in xrange(tests):
	N = int(raw_input())

	print get_smallest_number(N)