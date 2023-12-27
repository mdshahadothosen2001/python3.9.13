#convert to ascii code value from a character
a = "a"
ascii_of_a = ord(a)
print(ascii_of_a)

# convert to ascii value from the strings name
name = "Md. Shahadot Hosen"
ascii_of_name = [ord(w) for w in name]
print(ascii_of_name)
print(sum(ascii_of_name))
