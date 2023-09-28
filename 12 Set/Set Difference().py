# difference() is  a method
# Operator is '-'
# difference is # [ matrix, set function like( A u B) , (A∩B), A-B,Á, U-A]

# Difference means remove iteams
# A-B
# here A={1,2,3,4}  and B={5,8,9,3,2}

# A-B ={1,2,3,4}-{5,8,9,3,2}={1,4}
# result is {1,4}

a={1,2,3,4}
b={5,8,9,3,2}
c=a.difference(b)
print(c)
# display only uncommon value at only first set()


# another syntax
# c=a-b
print(a-b)