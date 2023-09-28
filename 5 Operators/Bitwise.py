# Bitwise (and &) (or | ) (not ~) (XOR ^) (Right shift >>) (Left Shift <<)


# 10 = 1010 (in Binary)
#        1010
#        1010
#    ------
# 10 & 10 is   1010 = 10
# ---------------- 
# 10 | 10 is   1010=10 
# --------------- 
# 10 ^ 10 is  0000 =0 

#  ~ 10 is  where 0=1 and 1=0 implement , 10=1010(in Binary ) now ~10=0101
#  ~10=0101  here 11=1011 now -11 = 0101  (using 2's complement) 
# Finally we get ~10 == -11


# Shift first right sift 
# use a>>2 here a binary bit value right shift for 2 bit
# a=10, 10=1010(in Binary) 
# shift Zero from right side 0 ->  1010 -> [] here shift 0ne bit value from this
# now                       [] ->  0101 -> 0   here right shift one bit that's 0 value
# one more Becase use 2     0 ->   0101 -> [] 
#                           [] ->  0010 -> 1 shift one more bit value that's 1
#                                  0010 =  2


# Left shift similar process just shift bit value Left side from binary values
#                    1010
#               [][] <- 1010 <- 00
#               00   <- 1000 <- [][]
#                       1000=40
a=10
b=10
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(~11)
print(a>>2)
print(a<<2)