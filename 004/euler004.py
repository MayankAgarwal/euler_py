def isPalindrome(num):

    num = str(num)

    if num[::1] == num[::-1]:
        return True
    return False


def getPalindromes ():

    palindromes = set()
    MIN_PALINDROME = 10**5
    MAX_PALINDROME = 10**6

    for i in range(100, 1000):
        for j in range(100, i+1):

            temp = i*j

            if MIN_PALINDROME < temp < MAX_PALINDROME and isPalindrome(temp):
                palindromes.add(temp)

    return palindromes


precomputed_palindromes = getPalindromes()

tests = int(raw_input())

for test in xrange(tests):

    N = int(raw_input())

    result = -1

    for p in precomputed_palindromes:
        if p < N and result < p:
            result = p

    print result