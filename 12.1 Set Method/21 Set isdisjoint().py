# isdisjoint method is a
# if no common then True ,otherwise False
a={1,2,3,4,6}
b={2,4,6}

print(a.isdisjoint(b))
# Display False
print(b.isdisjoint(a))
# Display False

a={1,2,3}
b={6,7,8}
print(a.isdisjoint(b))
# display True

# Because here is no one common items in a,b