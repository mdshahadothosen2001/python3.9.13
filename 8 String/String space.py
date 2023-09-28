a="Hello"
c="{0:<20} World".format(a)
print(c)


# for centree

c="{:^30}World".format(a)
print(c)

c="{0:>22} {0}".format(a)
print(c)

c="{0:*<12}".format(a)
print(c)