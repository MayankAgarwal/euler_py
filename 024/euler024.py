def __init_break_indices__(num):

    indices = [1]*num

    for i in xrange(1, num):
        indices[num-1-i] = indices[num-i]*i

    return indices

def get_lex_permutation (N, base_string, break_indices):

    stringPermutation = []
    divident = []
    base_string = list(base_string)
    divident_prefix = 0

    for i in xrange(len(base_string)):

        if (i-1) >= 0:
            temp = ( N - 1 - divident_prefix )/break_indices[i]
        else:
            temp = ( N - 1 )/break_indices[i]

        temp_int = int(temp)

        stringPermutation.append(base_string[temp_int])
        base_string.pop(temp_int)
        divident_prefix += temp_int*break_indices[i]


    return ''.join(stringPermutation)



__STRING = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
__BREAK_INDICES = __init_break_indices__(len(__STRING))

tests = int(raw_input())

for test in xrange(tests):
    N = int(raw_input())

    print get_lex_permutation(N, __STRING, __BREAK_INDICES)