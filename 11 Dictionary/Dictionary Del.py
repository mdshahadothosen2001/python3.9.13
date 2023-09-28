# Here we Analysis for delete items of Dictionary
# We can deleted using How many way 
a={'one':'Md.','two':'Shahadot','three':'Hosen','end':'2001'}


# If we use del(a)
# then deleted variable
# We don't need to delete variable , we want deleted only items
# # del(a)
# print(a)

# using del(a[key])

# 1.No.Way
del(a['end'])
print(a)
# Successfully deleted one item by key

# using variable.pop(a[key])

# 2.No.Way
a.pop('three')
print(a)

#using pop() method
# Again.2.No.Way for nested
# for nested Dictionary
a={'one':'Md.',
'two':'Shahadot',
'three':'Hosen',
'four':{1:'software',
2:'Engineer',
3:'engineer'
} 
}
#a[item-key of dictionary].pop(item-key of nested dictionary)
a['four'].pop(2)
print(a)


# using popitem method
# forn delete
# when we don't given argument then 
# deleted one item from ending of dictionary

#3.No.Way
a.popitem()
print(a)

# popitem with no argument


