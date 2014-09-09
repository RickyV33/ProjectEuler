from math import sqrt

def largestPrimeFactor(num = 600851475143):
    """Returns the largest prime factor of a given number.
    num defaults to 600851475143 if no argument is given."""

    divisor = 2 #Holds the divisor that num is divided by

    while divisor <= sqrt(num):
        if num % divisor == 0:
            num /= divisor
        else:
            divisor = 3 if divisor == 2 else divisor + 2 #Only uses divisors 2,3,5,7,9,11....(n+2)

    return num


if __name__ == '__main__':
    print "Largest prime factor of 13195:", largestPrimeFactor(13195)
    print "Largest prime factor of 600,851,475,143:", largestPrimeFactor()
