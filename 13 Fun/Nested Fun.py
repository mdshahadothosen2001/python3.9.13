# nested fun

def sweet():
    print('Sweet Heart')
    def heart():
        print("hey sweet heart")
# call first def
print(sweet())
# we can not call inner def at out of main def
# so we call inner def fun
def sweet():
    print('Sweet Heart')
    def heart():
        print("hey sweet heart")

    heart()    
print(sweet())        