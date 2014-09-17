def isPrime(num):
    """Returns True if num evaluates to a prime number, returns false otherwise."""

    divisor = 2 #Holds the divisor that num is divided by

    while divisor < num:
        if num % divisor == 0:
           return False
        else:
            divisor = 3 if divisor == 2 else divisor + 2 #Only uses divisors 2,3,5,7,9,11....(n+2)

    return True

def findNthPrime(N):
    """Finds the Nth prime number from 0.
    Returns the Nth prime number if it exists, otherwise return 0"""

    b = 2
    counter = 1 #Keeps track of the prime count. Starts at 1 to count 2 as prime

    while counter < N:
        if isPrime(b):
            counter += 1
        b = 3 if b == 2 else b + 2 #Only uses odd numbers besides 2 (2,3,5,7,9...)

    return b


if __name__ == "__main__":
    print "The 6th prime number is:", findNthPrime(6)
    print "The 10,001th prime number is:", findNthPrime(10001)
