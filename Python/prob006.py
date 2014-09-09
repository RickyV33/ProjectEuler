def sumOfSquares(start = 1, end = 101):
    """Returns the sum of all the squares between start and end.
    start and end default to 1 and 101 respectively if no arguments are passed in.
    Note that it will only iterate through end-1"""

    #Square each iteration and then sum all the iterations together
    return sum((x*x for x in xrange(start, end))) 

def squareOfSums(start = 1, end = 101):
    """Returns the square of the sum of all the numbers between start and end.
    start and end default to 1 and 101 respectively if no arguments are passed in.
    Note that it will only iterate through end-1."""

    #Sum each iteration and then square the sum 
    return pow(sum(x for x in xrange(start, end)), 2)

def sumSquareDifference(start = 1, end = 101):
    """Returns the difference of the square of the sums and the sum
    of the squares between start and end. 
    start and end defaults to 1 and 101 respectively if no arguments are passed in.
    Note that it will only iterate through end-1"""

    return  squareOfSums(start, end) - sumOfSquares(start, end)


if __name__ == "__main__":
    print "From 1 to 10: ", sumSquareDifference(1, 11)
    print "From 1 to 100: ", sumSquareDifference()
