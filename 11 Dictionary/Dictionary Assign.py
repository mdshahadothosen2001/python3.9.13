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


# 4 No.is:
# string key
a={'first':'Md.',
   'midle':'Shahadot',
   'last':'Hosen' 
  }
# use karlibraches
# Assign value of variable
print(a)



# 5 No.is:
# Integer key 
# Assign value of variable
# use karlibraches

a={1:'Md.',
   2:'Shahadot',
   3:'Hosen'
  }
# Access items of dictionary
print(a)

# 6 No.is:
# Mixed key
# Use karlibraches

a={'First':'Md.',2:'Shahadot',3:'Hosen','Year':2001}
#Display items of Dictionar
print(a)