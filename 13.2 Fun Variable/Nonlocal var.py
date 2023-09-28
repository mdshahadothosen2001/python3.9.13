# nonlocal use for Nested Fun

def BD():
    a=12
    def Bogura():
        a=10
        print("Bogura",a)
    Bogura()
    print('BD',a)

# we can not changle value globally
# because a is a local for BD and a is a local for Bogura

BD()        
#so define as a non local
# then we can change value globally
# using 'nonlocal' keyword

def BD():
    a=12
    def Bogura():
        #nonlocal a
        a=10
        print('Bogura',a)
    Bogura()
    print('BD',a)

BD()