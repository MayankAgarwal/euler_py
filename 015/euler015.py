def get_possible_paths(N, M):

	UPPER_LIMIT = 10**9 + 7

	maze_points = [ [1 for x in xrange(M+1)] for y in xrange(N+1)]
	maze_points[0][0] = 0

	for i in xrange(1, N+1):
		for j in xrange(1, M+1):
			maze_points[i][j] = maze_points[i-1][j] + maze_points[i][j-1]

	for i in xrange(1, N+1):
		for j in xrange(1, M+1):
			maze_points[i][j] = maze_points[i][j]%UPPER_LIMIT

	return maze_points


N_MAX = 500
M_MAX = 500

maze_points = get_possible_paths(N_MAX, M_MAX)

tests = int(raw_input())

for test in xrange(tests):

	N, M = map(int, raw_input().split(' '))

	print maze_points[N][M]