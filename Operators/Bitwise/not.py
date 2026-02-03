# not symbol : ~

# it invert all bits 

# it's binary value
# their decimal numbers :
#  no   1 2 4 
#  2    0 1 0
#  3    1 1 0
#  4    0 0 1
#  5    1 0 1
#  6    0 1 1
#  7    1 1 1

# according and bitwise operator if each decimal binary's code one bit match it then it count it as one else it consider zero
# example
#it return value :

# 6 binary code : 0 1 1
# 4 binary code : 0 0 1
# invert of 6   : 1 0 0
# invert of 4   : 1 1 0
#-------------------------
# 1 and 1 match : 0 1 0
# result : 2

# make it both decimal binary code into not
# perform xor
print(~6^~4) 