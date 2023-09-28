# sort don't work when have string and integer both
# sort by ASCII Code(UNI CODE)

# Sort Acending Order

a=[3,8,9,7,2,1]
a.sort()
print(a)

a=['Md.','Shahadot','Hosen','A']
a.sort()
print(a)

# Sorting Disending Order

a=[1,5,7,3,9,4,17]
a.sort(reverse=True)
print(a)


# Sorting by Lenght

a=['Hello','Sweet Heart','Tell','Me','Your Sweet','Name Please']
 # Sorting by Lenght with Acending Order
a.sort(key=len)
print(a)

 # Sorting by lenght with Dicending Order
a=['Hello','Sweet Heart','Oi','Sweet','Heart','Tell','Me','Your Sweet','Name Please']

a.sort(reverse=True,key=len)
print(a)