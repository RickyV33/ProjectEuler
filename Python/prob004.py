def largestPalindromeProduct(min = 100, max = 1000):
    """Finds the largest palindrome in the range of min and max.
    min and max defaults to 100 and 1000 respectively if no argument is passed in."""
    
    palindrome = 0 #Holds the palindrome of the product between numbers

    for x in range(min, max):
        for y in range(min, max):
            product = x*y
            if checkPalindrome(product) and palindrome < x*y:
                palindrome = product
    
    print palindrome
    
def checkPalindrome(num):
    """Checks if num is a palindrome. 
    If num is a palindrome, return True, otherwise return False"""

    return str(num) == str(num)[::-1] #Compares string num with a reversed string num

if __name__ == "__main__":
    largestPalindromeProduct()
