def merge(arr1, arr2):

    i1 = 0
    i2 = 0
    
    merged_array = []

    while i1<len(arr1) and i2<len(arr2):
        if arr1[i1] < arr2[i2]:
            merged_array.append(arr1[i1])
            i1 += 1
        else:
            merged_array.append(arr2[i2])
            i2 += 1

    merged_array.extend(arr1[i1:])
    merged_array.extend(arr2[i2:])

    return merged_array

def merge_sort(array):

    if len(array) <= 1:
        return array

    mid = int(len(array)/2)

    left_sorted = merge_sort(array[:mid])
    right_sorted = merge_sort(array[mid:])

    return merge(left_sorted, right_sorted)


def get_character_score(name):
    
    name = name.upper()
    score = 0

    for character in name:
        score += (ord(character) - 64)

    return score


N = int(raw_input())
names = []

for n in xrange(N):
    names.append(raw_input().strip().upper())

names = merge_sort(names)

Q = int(raw_input())

for query in xrange(Q):
    score = 0

    query_name = raw_input().strip().upper()

    score = (names.index(query_name) + 1) * get_character_score(query_name)

    print score