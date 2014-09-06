def sumEvenFibNumbers(num = 4000000):
    """Finds the sum of all even fibonacci numbers below num.
    num defaults to 4 million if no argument is given."""
    
    x, y = 0, 1
    total = 0

    while x <= num:
        if x % 2 == 0:
            total += x
        x, y = y, y+x

    print total

if __name__ == '__main__':
    sumEvenFibNumbers()
