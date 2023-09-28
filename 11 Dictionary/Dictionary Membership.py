#We discuss->previus
a={'one':'Md.','two':'Shahadot','three':'Hosen'}
#check by membership concept
print('shahadot' in a)
# display->False
# because 'shahadot' not in here this dictionary as a Key

# membership concept check by key
print('one' in a)
#display is True

#we can handle Nested dictionary
a={'one':'Md.',
'two':'Shahadot',
3:'Hosen',
'four':{1:2001,2:99}
}

print(2 in a)
# Display -> False
# Because direct not enter nested dictionary
# use first key then enter nested key

print(2 in a['four'])
#Display->True
