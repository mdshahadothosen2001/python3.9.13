# two way for copy dictionary items assign

# one is
a={1:'Md.',2:'Shahadot',3:'Hosen'}
b=a;
print(a,b,sep='\n')

# another one is
# using copy() method

c=b.copy()
print(c)

# Nested dictionary handle
a={1:'Md.',
2:'Shahadot',
3:'Hosen',
4:{5:'Md.',6:'Shahadot',7:'Hosen'}
}
d=a[4].copy()
print(d)
# finaly copied from nested dictionary