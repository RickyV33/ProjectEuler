def specialPythTriplet(num=1000):
    """Returns the product of three pythagorean triplets that have
    a sum of num. num defaults to 1000 if no argument is passe in."""
    for i in xrange(1, num):
        for j in xrange(1, num):
            k = num - i - j #Since i + k + j == 1000 
            if (i**2 + j**2 == k**2):
                return k*j*i

if __name__ == "__main__":
    print "Product of pythagorean triplets with a sum of 1000:", specialPythTriplet(1000)
