# fun def
def sohan(x,y):
    print(x,y)
# another fun def    
def sweet(a,b):
    print(a,b)    

# 
#     
i=8
j=10
sohan(i,j)
sweet(i,j)


# Here i,j are Global variable
# because we can use anywhere
# like use 'sohan()' fun and also use 'sweet()' fun



# we can use fun var 
# for use keyword 'global'
def BD():
    global z
    z=40
    print(x,y,z)
def Urop():
    k=12
    print(x,y,z)
x=12
y=14
z=0    
print(x,y,z)
BD()
Urop()
print(x,y,z)        
