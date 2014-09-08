def sumEvenFibNumbers(num = 4000000):
    """Finds the sum of all even fibonacci numbers below num.
    num defaults to 4 million if no argument is given."""
    
    x, y = 0, 1 #Holds n-1 and n in the fibonacci sequence respectively
    total = 0 #Holds the total sum of all the even fibonacci numbers

    while x <= num:
        if x % 2 == 0:
            total += x
        x, y = y, y+x

    print total

if __name__ == '__main__':
    sumEvenFibNumbers()
