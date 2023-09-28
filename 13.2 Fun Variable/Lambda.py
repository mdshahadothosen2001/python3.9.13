# Anonymous function
# lambda means here is no name for function
# Syntax: lambda arguments : expression
# have only one expression
# here more argument

# normally def
def BD(a,b):
    print(a+b)
BD(12,45)

# Lambda fn
x=lambda a,b:print(a+b)
# we can use only 1 line
x(12,46)

# there have default return
x=lambda a,b:a+b
i=x(12,47)
print(i)


# one more 
print((lambda a,b:a+b)(12,48) )


# most use

def bd(a):
    return lambda b:a+b
x=bd(12)
print(x(2))
