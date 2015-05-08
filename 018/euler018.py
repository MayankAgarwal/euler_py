def get_max_path_sum(triangle):

	for i in xrange(len(triangle)-2, -1, -1):
		for j in xrange(len(triangle[i])):

			sum1 = triangle[i][j] + triangle[i+1][j]
			sum2 = triangle[i][j] + triangle[i+1][j+1]

			triangle[i][j] = max(sum1, sum2)


	return triangle[0][0]



tests = int(raw_input())

for test in xrange(tests):

	N = int(raw_input())

	triangle = []

	for line in xrange(N):
		triangle.append(map(int, raw_input().strip().split(' ')))

	print get_max_path_sum(triangle)
