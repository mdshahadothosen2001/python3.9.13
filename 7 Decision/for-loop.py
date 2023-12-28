#   for variable_name in sequence
#Syntax  for for loop:
#  for (variable_name) in range(limit_variable_name)


# kind of one
i=0
j=4
for i in range(j):
   print(i)

    
# another  when we don't defined value for loop variable, start value (0) zero
for i in range(4):
    print(i)


# another format with start and end value
for a in range(5,10):
    print(a)


# another format with start and end and increasing value
for a in range(5,20,2):
    print(a)


# string array use (item in array_variale_name)
need=["color pen","pencil","ereser","supner","a4 page"]
for item in need:
    print(item)


## index and item both are iterable
for i,item in enumerate(need):
    print(item,":",i)


# iteration with condition
n=9
for a in range(n):
    if  a%2==0:
        print(a," This is Even Number")
    else:
        print(a," This is Odd Number")


# inline loop
english = [1,2,3,5]
french = [3,5,3,2]

new_for_english = [i for i in english]
print(new_for_english)


# inline loop with condition find common item
resut = [x for x in english if x in french]

print(resut)
