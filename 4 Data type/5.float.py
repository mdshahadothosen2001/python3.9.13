
a=89.12345678900123456789
print(a,type(a))

a=9876.012345678901234
print(a)

a=98.123456
print("{:.2f}".format(a))

a = 5
b = 2
c = a / b
c = round(c, 5)
formatted_c = format(c, '.5f')

# expected 2.50000
print(formatted_c)


"""min_diff is initialized to the positive infinity value. 
In Python, float('inf') represents positive infinity, 
which is a special floating-point value that is greater than any finite number."""

initial_infinite_val = float('inf')
print(initial_infinite_val)
