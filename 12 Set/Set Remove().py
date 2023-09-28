# we can't delete specific items by index because set is a unindex and unordered
a={'Md.','Shahadot','Hosen',2001,11}
a.remove(11)
# remove by value
print(a)

# we can delete all items
a.clear()
print(a)

# use discard( ) method
a={1,2,3,'md'}
a.discard('md')
print(a)

# remove vs discard
# when use remove() method and pass argument for delete but
#  which is not have in this set() then display Error 
# but discard display not error
a={'Md.','Shahadot','Hosen'}
# if we use this ,display error
# a.remove('Sohan')
print(a)
a.discard('sohan')
print(a)
# display all items of set() without any Error