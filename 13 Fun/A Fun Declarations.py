# Uder define functions declaration
# functions declare by 'def'

# syntax: def fun_name():
#                  statement 1
#                  statement 2
#                   .......
#                   statement n



# For Example:
def sohan():
    print('Md. Shahadot Hosen')
    print('Software Engineer')
    print('Born Bogura BD')

sohan()    


# More one
# user def with no argument
# argument , parameter is same

def summations():
    b=int(input('Enter a integer Number: '))
    c=int(input('Enter a integer number: '))
    a=b+c
    print('Summation is: ',a)

summations()    


# user def with argument
def differ(a):
    a=int(a-2)
    print(a)
a=12
# reference by value
differ(a)
# direct pass value
differ(24)
# pass float
differ(34.9)
# Default argument
def mul(a=10):
    a=int(a*2)
    print(a)
x=30
mul()
mul(x)


# fun with return
def ret():
    a=10
    b=10
    c=int(a+b)
    return c
    #return 'Hey'

x=ret()
print(x)     


# reference by address
# when passing value for *variable
# then create and set value as a Class Tuple() by default 
def assign(*n):
    print(n)

x=int(4)
assign(x)
assign(3,4,5,6,7)

# Argument as a key
# same name for key argument
def string(item1,item2,item3):
    print(item1,item2,item3,sep='\n')
#key argument
string(item1='Banana',item2=20,item3='40k')  
# key argument unsorted
string(item3='60k',item1='Banana',item2=30)
# non key argument and key argument
# we can non key argument Left side, not midle,no right 
string(30,item2='Banana',item3='40k')


# **keyword Argument
# display as a dictionary{}
# have 'key:value'
# access by key, not index
def sohan(**love):
    print(love)
    print('only one key value: ',love['my'])

sohan(item='sweet',item2='heart',item3='my',my='Tell me your sweet name pls')


