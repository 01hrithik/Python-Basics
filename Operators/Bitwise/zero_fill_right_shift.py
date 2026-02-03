# zero fill right shift symbol : >>

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

# after using right fill zero binary code will be :

# before added right zero :
#  no  0  1  2  4  8  16 
#  2   0  0  1  0  0  0
#  3   0  1  1  0  0  0
#  4   0  0  0  1  0  0
#  5   0  1  0  1  0  0
#  6   0  0  1  1  0  0
#  7   0  1  1  1  0  0

# after right shift
# no  16  8   4   2   1
# 2   0   0   0   0   0   
# 3   0   0   0   0   0   
# 4   0   0   1   0   0   
# 5   0   0   1   0   1   
# 6   0   0   1   1   0   
# 7   0   0   1   1   1   

 


# example 
# return value :
# 7 binary code : 0 0 1 1 1
# 2 binary code : 0 0 0 0 0
# --------------------------
# result        : 1
# becuse right shift divided by n times right shift
print (int(3/2))
print(7>>2)
