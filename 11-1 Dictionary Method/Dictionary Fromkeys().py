# handle by key
# first define one diction and that have some value
# this value defined as a keys
# then set value by these keys

a=('name','id','phone')
print(a)
#display for check 1
b=dict.fromkeys(a)
print(b)
# Assign these items as a keys to 'b' from 'a'


# set value
c={'name':'Md. Shahadot Hosen',
   'id':20001,
   'phone':+8801942387768
  }
#update data 'assign only value

b.update(c)
#updated by 'c' values
print(b)
# Display updated values
