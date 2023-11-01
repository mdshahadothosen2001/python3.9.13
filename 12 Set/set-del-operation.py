s = {1,2,3,4,5,6,7,8,9}
#del first item
s.pop()

# del specific item
s.remove(5)
# can not del if item not in
#s.remove(10)

#del specific item
s.discard(8)
#return none if item not in
s.discard(10)

print(s)