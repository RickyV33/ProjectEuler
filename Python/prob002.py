def sumEvenFibNumbers(num = 4000000):
    """Returns the sum of all even fibonacci numbers below num.
    num defaults to 4 million if no argument is given."""
    
    x, y = 0, 1 #Holds n-1 and n in the fibonacci sequence respectively
    total = 0 #Holds the total sum of all the even fibonacci numbers

    while x <= num:
        if x % 2 == 0:
            total += x
        x, y = y, y+x
        
    return total

if __name__ == '__main__':
    print "Sum of first 10 even fibonacci terms:", sumEvenFibNumbers(10)
    print "sum of first 4,000,000 even fibonacci terms:", sumEvenFibNumbers()
