def get_digit_sum(num):
	str_num = map(int, list(str(num)))
	return sum(str_num)


tests = int(raw_input())

for test in xrange(tests):

	N = int(raw_input())

	digit = 2**N

	print get_digit_sum(digit)