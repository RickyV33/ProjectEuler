def greatestCommonDivisor(numA, numB):
    """Returns the greatest common divisor between numA and numB.
    Continues until numB is equal to 0 (base case), leaving numB equal
    to the common divisor."""

    while numB is not 0:
        numA, numB = numB, numA % numB

    return numA

def leastCommonMultiple(numA, numB):
    """Returns the least common multiple between numA and numB.
    Uses the algorithm lcm(a, b) = (a * b) / gcd(a, b)"""

    multiple = 2 #Holds the least common multiple

    for i in xrange(numA, numB):
        multiple = (i * multiple) / greatestCommonDivisor(i, multiple)

    return multiple


if __name__ == "__main__":
    print "Least common multiple between 1 and 10:", leastCommonMultiple(1, 11)
    print "Least common multiple between 1 and 20:", leastCommonMultiple(1, 21)
