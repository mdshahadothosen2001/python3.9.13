

#from tkinter import scrolledtext


a=19

if a>10:
       print("This value greater than 10")
else:
    print("This value is Less or equal ") 

# implement on one line

print("Greater") if a>10 else print("Less or equal")  

# we can this ternary operators assign another variable

a= "Greater than " if a>10 else "Less or equal"
print(a)