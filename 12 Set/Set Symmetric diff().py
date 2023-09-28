# Symmetric Difference is a method
# operator is '^'
# [ matrix, set function like( A u B) , (A∩B), A-B,Á, U-A]


# symmetric means only uncommon values
a={1,2,3,8,9,11}
b={2,3,4,5,9,8,15}
c=a.symmetric_difference(b)
print(c)
# display only uncommon items from both set


# another syntax
# c= a^b
print(a^b)
