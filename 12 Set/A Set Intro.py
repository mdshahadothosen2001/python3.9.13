# als ouse use '{}' for Set
# previus->'{}' for Dictionary
# previus->'[]' for List
# previus->'()'for Tuple
# previus->' " " ' for String


# Set() is a -> unodered . no duplicate value. no work by index
# we can not use all data in Set()
# like Dict{},Nested Set{},List[]
# only use limited like string,int,float,Tuple()

#firstly declare a Set
#always '{}' default as a dictionary
#when here have 'key:value' is a dict
#but when here is only value as a sinlge item is a 'Set()' like->
# a={'one','two','thre'} is a Set()
#here a is a dict
a={}
print(a,type(a))
#declare key with value
a={1:'one','two':2,'three':3}
print(a,type(a))
#now declare for single value
a={'Md.','Shahadot','Hosen'}
print(a,type(a))
# finaly got as a Set()


# set()-> unodered
a={'Md.','Shahadot','Hosen'}
#display same arrange or sorted arrange
print(a)
# for check odered 
# use list
a=['Md.','Shahadot','Hosen']
# display same arrange
print(a)

# Set accept no same items |\\||\ no duplicate value
a={'Md.','Shahadot','Hosen','Shahadot'}
print(a)

# we can not use all data
a={'Md.',
   'Shahadot',
   3,
   5.9,
   ('Md.','Shahadot','Hosen'),
  # ['Md.','Shahadot','Hosen'], not use list[] in set{}
  # {'Md.','Shahadot','Hosen'}, not use Set{} in  set{}
  # {1:'Md.',2:'Shahadot',3:'Hosen'} not use dict{} in set{}

}
print(a)
