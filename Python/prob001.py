def sumMultiplesOfThreeAndFive(num = 1000):
    """Finds the sum of all natural numbers below num that is a multiple of 3 or 5.
    num defaults to 1000 if no argument is given."""

    print sum([x for x in range(num) if x % 3 == 0 or x % 5 == 0])

if __name__ == '__main__':
    sumMultiplesOfThreeAndFive()
