for test in range(input()):

    N = input()

    N3 = int( (N-1)/3 )
    N5 = int( (N-1)/5 )
    N15 = int( (N-1)/15 )

    S3 = ( 3 * N3 * (N3+1)) / 2
    S5 = ( 5 * N5 * (N5+1)) / 2
    S15 = ( 15 * N15 * (N15+1)) /2

    sum = S3 + S5 - S15

    print sum
