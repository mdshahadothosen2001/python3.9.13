# first difference and then update at first set

# first difference
a={1,2,3,4}
b={1,2,6,8}
print(a.difference(b))
# display

print(a.difference_update(b))
# display 'None'
a={1,2,3,4}
b={1,2,6,8}
print(a.difference_update(b),a,b,sep='\n')
# now display updated set in a