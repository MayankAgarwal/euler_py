N = int(raw_input())

result = 0
o_11_digit = 0
o_12_digit = 0

for i in xrange(N):

	num = list(raw_input())

	first_ten_digits = int(''.join(num[0:10]))
	temp_11_digit = int(num[10])
	temp_12_digit = int(num[11])

	o_12_digit = o_12_digit + temp_12_digit

	temp_11_carryover = int(o_12_digit/10)
	o_12_digit = o_12_digit%10

	o_11_digit = o_11_digit + temp_11_carryover + temp_11_digit

	temp_carryover = int(o_11_digit/10)
	o_11_digit = o_11_digit%10

	result += first_ten_digits + temp_carryover


str_result = str(result)[0:10]

print ''.join(str_result)