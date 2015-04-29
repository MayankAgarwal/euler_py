class disallowNegativeIndex(object):

	def __init__(self, obj):
		self._obj = obj
		self.__default = 1

	# Return 1 if matrix index out of bounds.
	def __getitem__(self, (i, j)):
		if isinstance(i, int) and isinstance(j, int):
			if i<0 or j<0:
				return self.__default
			elif i>=20 or j>=20:
				return self.__default
			else:
				return self._obj[i][j]


def get_max_multiple(matrix):

	result = 0
	matrix_wrapped = disallowNegativeIndex(matrix)

	for i in xrange(20):
		for j in xrange(20):

			up_mul = matrix_wrapped[i,j] * matrix_wrapped[i-1, j] * matrix_wrapped[i-2, j] * matrix_wrapped[i-3, j]
			down_mul = matrix_wrapped[i, j] * matrix_wrapped[i+1, j] * matrix_wrapped[i+2, j] * matrix_wrapped[i+3, j]
			left_mul = matrix_wrapped[i, j] * matrix_wrapped[i, j-1] * matrix_wrapped[i, j-2] * matrix_wrapped[i, j-3]
			right_mul = matrix_wrapped[i, j] * matrix_wrapped[i, j+1] * matrix_wrapped[i, j+2] * matrix_wrapped[i, j+3]

			left_up_diag_mul = matrix_wrapped[i, j] * matrix_wrapped[i-1, j-1] * matrix_wrapped[i-2, j-2] * matrix_wrapped[i-3, j-3]
			right_up_diag_mul = matrix_wrapped[i, j] * matrix_wrapped[i-1, j+1] * matrix_wrapped[i-2, j+2] * matrix_wrapped[i-3, j+3]
			left_down_diag_mul = matrix_wrapped[i, j] * matrix_wrapped[i+1, j-1] * matrix_wrapped[i+2, j-2] * matrix_wrapped[i+3, j-3]
			right_down_diag_mul = matrix_wrapped[i, j] * matrix_wrapped[i+1, j+1] * matrix_wrapped[i+2, j+2] * matrix_wrapped[i+3, j+3]

			temp = max(up_mul, down_mul, left_mul, right_mul, left_up_diag_mul, right_up_diag_mul, left_down_diag_mul, right_down_diag_mul)

			if temp > result:
				result =temp

	return result




matrix = []

for i in xrange(20):
	matrix.append(list(map(int, raw_input().split(' '))))

print get_max_multiple(matrix)