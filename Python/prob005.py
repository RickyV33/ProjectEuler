def greatestCommonDivisor(numA, numB):
    """Finds the greatest common divisor between numA and numB.
    Continues until numB is equal to 0 (base case), leaving numB equal
    to the common divisor.
    Returns the greatest common divisor."""

    while numB is not 0:
        numA, numB = numB, numA % numB
    return numA

def leastCommonMultiple(numA, numB):
    """Finds the least common multiple between numA and numB.
    Uses the algorithm lcm(a, b) = (a * b) / gcd(a, b)"""

    multiple = 2 #Holds the least common multiple

    for i in range(numA, numB):
        multiple = (i * multiple) / greatestCommonDivisor(i, multiple)

    print multiple


if __name__ == "__main__":
    leastCommonMultiple(1, 21)
