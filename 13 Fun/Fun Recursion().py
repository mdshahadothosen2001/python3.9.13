# def sohan():
#        sohan()  //call in onwself fun that's recursion
#
#print(sohan())

# call onwself

def sohan(n):
    if(n==10):
        return n
    else:
        return sohan(n+1)
        # call 'sohan()' fun passing value before increment

print(sohan(3))
















