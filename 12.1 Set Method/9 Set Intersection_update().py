
# first display as a intersection
a={1,2,4,6,8}
b={3,4,5,6,9}
print(a.intersection(b))

# now using
# intersection_update
print(a.intersection_update(b))
# display None
# because update and store at a
# now display
a={1,2,4,6,8}
b={3,4,5,6,9}
print(a.intersection_update(b),a,b,sep='\n')