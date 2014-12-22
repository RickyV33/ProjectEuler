import math

def sumOfPrimes(limit=2000000):
    """Returns the sum of primes below limit using Sieve of Eratosthenes."""
    numbers = range(limit+1)
    numbers[1] = 0
    limitRange = int(math.sqrt(limit)) + 1 #
    for i in xrange(2, limitRange): #Only iterates through the square root of limit
        if numbers[i] > 0:
            for j in xrange(i*i, limit+1, i): #Remove all multiples of i from numbers list starting at i^2
                numbers[j] = 0

    return sum(numbers)

if __name__ == "__main__":
    print "Sum of primes below 2 million: ", sumOfPrimes()
    print "Sum of primes below 5 million: ", sumOfPrimes(5000000)
