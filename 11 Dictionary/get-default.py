fruits = {'apple':250, 'banana':110, 'orange':350}

# here 0 is defualt value

x = fruits.get('apple', 0)
y = fruits.get('banana', 0)
z = fruits.get('pear', 0)

print(x)
print(y)
print(z)
