a=['Md','Shahadot','Hosen','Software','Engineer']
for i in a:
    print(i)


b=['Md','Shahadot','Hosen',['Competitive','Programming','Algorithms','Number Theory','Graph','Math'], 'Software','Engineer']    

# Use fo nested list
# we can read, write under list in a list
for i in b:
    if type(i) is list:
        for j in i:
            print(j)