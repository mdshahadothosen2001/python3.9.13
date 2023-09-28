# freze

a={'Md.','Shahadot','Hosen'}
b={2001,5826}
a.update(b)
print(a)

# we can any item for add
# using any method

# when we don't want to change, remove,add...
# then use frozenset()
# then we can not change

c=frozenset(a)
print(c)
# display for check after freez
d={11,5}
# c.update(d)
# print(c)
# can not
#display for check , can we change?
