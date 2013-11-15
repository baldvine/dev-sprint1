# This is where Exercise 5.4 goes
# Name: Baldvin Einarsson

def is_triangle(a,b,c):
    #Convert to integers
    triSides=sorted([int(a),int(b),int(c)])
    #print triSides

    if (triSides[0]+triSides[1]>triSides[2]):
        print "Yes"
        return True
    else:
        print "No"
        return False

def checkTriangle():
    a=raw_input("Enter the first length: \n")
    b=raw_input("Enter the second length: \n")    
    c=raw_input("Enter the third length: \n")

    print "Can we form a triangle with those sides?\n"
    is_triangle(int(a),int(b),int(c))

checkTriangle()