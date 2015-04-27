def get_max_product(n,k, num):
    
    str_n = list(str(num))

    result = -1;

    for i in xrange(n-k):
        temp = 1

        for j in map(int, str_n[i:i+k]):
            temp = temp*j

        #temp = reduce(lambda x, y: temp + x*y, map(int, str_n[i:i+k]))

        if result < temp:
            result = temp

    return result



tests = int(raw_input())

for test in xrange(tests):

    N,K = map(int, raw_input().split(' '))
    num = int(raw_input())
    print get_max_product(N, K, num)
