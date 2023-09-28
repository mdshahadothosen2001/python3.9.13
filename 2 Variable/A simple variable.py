# Variable we can use (a to z),(A to Z),(0 to 9),(_)

Number_for_check=9
print(Number_for_check)

#Variable name just use (_)underscore
_=9
print(_)

#use uper case, lower case and number
number2ForCheck=19
print(number2ForCheck)


# mult variable
a,b,c,d,e,f=1,2,3,"Sinthiya",{1,2,3,4,5},{1,2,3,4,5,6}


print(a,b,c,d,e,f,sep="\n")

#delete one or more value
a,b,c,d,e,f=1,2,3,"Sinthiya",{1,2,3,4,5},{1,2,3,4,5,6}
del c,f
# c,f deleted value and variable 
# now if we want to print c,f (show massege is "NameError: name 'c' is not defined")
print(a,b,d,e,sep="\n")
