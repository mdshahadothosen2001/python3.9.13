# only one return
# can not more than one return using 'return'
def sohan():
    return 'hello'
    return 'world!'
for i in sohan():
    print(i)    





# multiple return
# use yield
def sohan():
    yield 'sweet'
    yield 'heart'
    yield 'tell'
    yield 'me'

# we can add more for return

for i in sohan():
    print(i)    
