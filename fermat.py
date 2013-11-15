#Exercise 5.3 in 'Think Python'

def check_fermat(a,b,c,n):
    if (pow(a,n)+pow(b,n)==pow(c,n)):
        if n>2:
            print "Holy smokes, Fermat was wrong!"
            return True
    else:
        print "No, that doesn't work"
        return False


check_fermat(2,3,4,6)