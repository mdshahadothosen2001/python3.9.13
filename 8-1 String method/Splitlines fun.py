# splitlines work for \n in string


a="Hey sweet heart\nTell me your sweet name please"
print(a)

# when use splitlines , don't work \n
#just display separate 
print(a.splitlines())
#when use True as a argument
#just show \n as a character but not work \n
print(a.splitlines(True))
#when False as a argument , not display \n , and not work \n, 
#work only splitlines()
print(a.splitlines(False))