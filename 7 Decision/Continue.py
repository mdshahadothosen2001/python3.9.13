# Here a=5 is missing 
# because when if statement get a==5 , for loop go next step for exicute 

b=10

for a in range(b):
    
    if a==5:
        continue
      
    print(a)


c=a+b
print("Summation is ",c)