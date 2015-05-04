corpus = {
	0 : "Zero",
	1 : "One",
	2 : "Two",
	3 : "Three",
	4 : "Four",
	5 : "Five",
	6 : "Six", 
	7 : "Seven",
	8 : "Eight",
	9 : "Nine",
	10 : "Ten",
	11 : "Eleven",
	12 : "Twelve",
	13 : "Thirteen",
	14 : "Fourteen",
	15 : "Fifteen",
	16 : "Sixteen",
	17 : "Seventeen",
	18 : "Eighteen",
	19 : "Nineteen",
	20 : "Twenty",
	30 : "Thirty",
	40 : "Forty",
	50 : "Fifty",
	60 : "Sixty",
	70 : "Seventy",
	80 : "Eighty",
	90 : "Ninety",
	100 : "Hundred",
	1000 : "Thousand",
	10**6 : "Million",
	10**9 : "Billion",
	10**12 : "Trillion"
}


def get_number_words (num):

	divisors = [10**12, 10**9, 10**6, 10**3, 10**2, 90, 80, 70, 60, 50, 40, 30, 20, 1]
	factors = []
	result = ""

	if num in corpus.keys():
		return corpus[num]

	for divisor in divisors:
		temp = int( num / divisor )
		num = int ( num % divisor )
		factors.append(temp)


	for pos in xrange(len(factors)):

		if factors[pos] == 0:
			continue

		if factors[pos] in corpus.keys():
			if divisors[pos] == 1:
				temp = corpus[factors[pos]]
			elif 1<divisors[pos]<100:
				temp = corpus[divisors[pos]]
			else:
				temp = corpus[factors[pos]] + " " + corpus[divisors[pos]]
		else:
			temp = get_number_words(factors[pos]) + " " + corpus[divisors[pos]]

		result = result + " " + temp

	return result.strip()


Tests = int(raw_input())

for test in xrange(Tests):

	N = int(raw_input())

	if N == 0:
		print "Zero"
	else:
		print get_number_words(N)