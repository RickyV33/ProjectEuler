import math

def isPrime(num):
    """Returns True if num evaluates to a prime number, returns false otherwise."""

    divisor = 2 #Holds the divisor that num is divided by

    while divisor < math.sqrt(num):
        if num % divisor == 0:
           return False
        else:
            divisor = 3 if divisor == 2 else divisor + 2 #Only uses divisors 2,3,5,7,9,11....(n+2)

    return True

def findNthPrime(N):
    """Returns the Nth prime number."""

    prime = 2 #Holds the prime number
    counter = 1 #Keeps track of the prime count. Starts at 1 to count 2 as prime

    while counter < N:
        if isPrime(prime):
            counter += 1
        prime = 3 if prime == 2 else prime + 2 #Only uses odd numprimeers primeesides 2 (2,3,5,7,9...)

    return prime


if __name__ == "__main__":
    print "The 6th prime number is:", findNthPrime(6)
    print "The 10,001th prime number is:", findNthPrime(10001)
