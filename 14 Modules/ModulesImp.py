# modules two types
#    1. User defined modules(create user)
#    2. Built in modules(have in py)

# Module means-> all file are module in python


# access data or variable from another file
# need to import
# use import keyword
import ModuleExp
print(ModuleExp.name)

ModuleExp.myself()

ModuleExp.summation(2,8)

# module name as a variable
import ModuleExp as m
m.myself()
m.summation(2,2)


# for only one fun import or variable access
# then use "from file name import fn_name,filr_name,_....."
# like, from ModuleExp import summation()