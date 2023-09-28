# just separate
# similar to rsplit
# split separate with remove argument
#but partition not remove argument line "Hoseb"
# divided 3 part only

a="Md. Shahadot Hosen Software Engineer"
print(a.partition('Hosen'))

# Here work only first sweet because only 3 part can separate
a="Hey sweet heart sweet heart"
print(a.partition('sweet'))


# when use rpartition work from right side
print(a.rpartition('sweet'))