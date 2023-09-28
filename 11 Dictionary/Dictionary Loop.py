a={'c1':'Md.',
    'c2':'Shahadot',
    'c3':'Hosen'
  }

# Loop handle
# using for Loop
for i in a:
    print(i)
# got only key
# Displayed only key

# we need values of items of dictionary

for i in a:
    print(a[i])
# here 'i' is value of key, like c1,c2,c3 for this dictionary
# using Dictionary key access concept

# another way to display items values

for i,j in a.items():
    print(i,'=',j)

# we can handle nested dictionary for 'Loop'           
