def largestPalindromeProduct(min = 100, max = 1000):
    """Returns the largest palindrome in the range of min and max.
    min and max defaults to 100 and 1000 respectively if no argument is passed in."""
    
    palindrome = 0 #Holds the palindrome of the product between numbers

    for x in xrange(min, max):
        for y in xrange(min, max):
            product = x*y
            if checkPalindrome(product) and palindrome < x*y:
                palindrome = product 

    return palindrome
    
def checkPalindrome(num):
    """Checks if num is a palindrome. 
    If num is a palindrome, return True, otherwise return False"""

    return str(num) == str(num)[::-1] #Compares string num with a reversed string num

if __name__ == "__main__":
    print "Largest palindrome from 2 digit numbers:", largestPalindromeProduct(10, 100)
    print "Largest palindrome from 3 digit numbers:", largestPalindromeProduct()
