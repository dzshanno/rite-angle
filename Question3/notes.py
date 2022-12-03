# The missing values a,b c,d e,f   and  are the digits 1,2 3,4 5   and 6 in some order.

# The numbers

# ab,c5d, e4f


# are in arithmetic progression.

# What is the maximum possible product for the three numbers? 

# To get your final answer, multiply this by 3.8 x 10-6  and take the integer part. 

# thoughts

# ab + c5d = e4f
# find max ab*c5d*e4f

import math
import itertools



allpossible = list(itertools.permutations(['1','2','3','4','5','6']))

inputs = []

for x in allpossible:
    inputs.append([(x[0]+x[1]),(x[2]+'5'+x[3]),(x[4]+'4'+x[5])])
    
maxproduct = 0

for y in inputs:
    print(y)
    if int(y[1])-int(y[0]) == int(y[2])-int(y[1]):
        product = int(y[0])*int(y[1])*int(y[2])
        if product > maxproduct:
            maxproduct = product
            print(y)
        
Result = maxproduct
Answer = int(Result * 3.8e-6)
print (Answer)
#answer is 27

