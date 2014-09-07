from math import sqrt

def largestPrimeFactor(num = 600851475143):
    """Finds the largest prime factor of a given number.
    num defaults to 600851475143 if no argument is given."""

    divisor = 2

    while divisor <= sqrt(num):
        if num % divisor == 0:
            num /= divisor
        else:
            divisor = 3 if divisor == 2 else divisor + 2 #Only uses divisors 2,3,5,7,9,11....(n+2)

    print num


if __name__ == '__main__':
    largestPrimeFactor()
