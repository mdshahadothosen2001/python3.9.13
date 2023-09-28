# When directly assign value at self function()
# Here use Dictionary function -> dict(here element)

# Constructor have 3 way


# one No.is:
#Karlibraches assign value of 'dict()'
a=dict({1:'Md.',2:'Shahadot',3:'Hosen'})
print(a,type(a))

# two No.is:
#Direct Assign without {},[],()
#Then use '='
b=dict(first='Md.',
       midle='Shahadot',
       last='Hosen'
)
print(b)

# 3 No.is:
# Assign as a pair of 'dict()' fun
# Use Braket
c=dict([('first','Md.'),
('midle','Shahadot'),
('last','Hosen'),
])
#Here divide by ',' comma
# taken first item for key and second item for value of first pair
# similarly taken
print(c)




