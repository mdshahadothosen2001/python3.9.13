# simple input 
a=input()
print("Your input value is ",a)


#taken name and id from employees
b=input("Enter Your Name: ")
c=input("Enter Your ID No: ")

print("Your Deails ",b,c,sep="\n")

#Type change 
b=input("Input your area code: ")
print(type(b))
c=int(b)
print(c)
y=type(c)
print(y)


#Input Multiple
#when use more than one variable for input one line
#use (dot )  .split() define space count 
a,b,c,d,e=input("Enter 5 value with space: ").split()
print(a,e,sep=" ")


#.plit() count by * 
a,b,c,d,e=input("Enter 5 value with * :").split("*")
#like 1*2*3*4*5
print(a,b,c,d,e,sep=" ")

#.split() count by space

a,b,c,d=input("Enter 4 value separate space").split(" ") 
print("{} {} {} {} ".format(a,b,c,d))