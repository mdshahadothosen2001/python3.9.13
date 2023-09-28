# we can not change string item
# but have different way



a="MD. Shahadot Hosen"
###a[1]="d"


# different way is

a=a[0:1]+"d"+a[2:]
print(a)

# successfully Done

