def sumMultiplesOfThreeAndFive(num = 1000):
    """Returns the sum of all natural numbers below num that is a multiple of 3 or 5.
    num defaults to 1000 if no argument is given."""

    return sum((x for x in xrange(num) if x % 3 == 0 or x % 5 == 0))

if __name__ == '__main__':
    print "Sum of the multiples of 3 and 5 below 10:", sumMultiplesOfThreeAndFive(10)
    print "Sum of the multiples of 3 and 5 below 1000:", sumMultiplesOfThreeAndFive(1000)
