#  setdefault method is a finding method
# or we can say one  kinds of taken one value only from dictionary
# or set one key or with value


# setdefault by key as a argument
a={'name':'Md. Shahadot Hosen','id':2001}
b=a.setdefault('id')
print(a,b,sep='\n\n')
# here taken id's value like 2001 

#sedefault by key which not have this dictionary

b=a.setdefault('email')
print(a,b,sep='\n\n')
# set new key  which given as a argument 
# set main dictionary
# here is no value for this argument's key
# so set 'None'

# setdefault by key:value as a argument
b=a.setdefault('born','Bogura')
print(a,b,sep='\n\n')
#set this argument as a key and value
# first argument set as a key and second set as a value
