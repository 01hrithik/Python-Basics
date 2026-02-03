# zero fill left shift symbol : <<

# left push zero

# it's binary value
# their decimal numbers :
#  no   1 2 4            
#  2    0 1 0
#  3    1 1 0
#  4    0 0 1
#  5    1 0 1
#  6    0 1 1
#  7    1 1 1 

# after using left fill zero binary code will be :
# as we read left to right simillar zero will be added to left to right each decimal binary's code zero 
# before added left zero :
#  no  0  1  2  4  8  16 
#  2   0  0  1  0  0  0
#  3   0  1  1  0  0  0
#  4   0  0  0  1  0  0
#  5   0  1  0  1  0  0
#  6   0  0  1  1  0  0
#  7   0  1  1  1  0  0

# after the add left zero :
# no  64  32  16   8  4   2   1
# 2   0   0   0   1   0   0   0
# 3   0   0   0   1   1   0   0
# 4   0   0   1   0   0   0   0
# 5   0   0   1   0   1   0   0
# 6   0   0   1   1   0   0   0
# 7   0   0   1   1   1   0   0



# example 
# return value :
# 7 binary code : 0 0 1 1 1
# 2 binary code : 0 0 0 1 0
# --------------------------
# result        : 28

print(7<<2)
