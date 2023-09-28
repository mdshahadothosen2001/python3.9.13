# We can not directly insert or append
# can not add item directly in tuple

# Can not change
# can not delete
a=('Md.','Shahadot','Hosen','Software')
print(a)
# a.append('Engineer')  this is not work
# a.insert(a)   this is not work

# if we want to change then
# we convert class tuple to class list
# Like bellow 
a=list(a)
print(a,type(a))
a.append('Engineer')
a.insert(4,'2001')
print(a)

# Now we can change,append,insert,delete as a class list
