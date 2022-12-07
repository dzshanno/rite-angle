# Question 2 - Stage 1
# a to j are the digits from 0 to 9 in some order.
# 1 divides the one-digit number a,
# 2 divides the two-digit number ab,
# 3 divides the three-digit number abc,

# 10 divides the ten-digit number abcdefghij.


# What is the ten-digit number  abcdefghij?

import math
import itertools

tendigit=[]
ninedigit=[]
eightdigit=[]
sevendigit=[]
sixdigit=[]
fivedigit=[]
fourdigit=[]
threedigit=[]
twodigit=[]
numbers=[]

def convertTuple(tup):
    st = ''.join(map(str, tup))
    return st

allpossible = list(itertools.permutations(['0','1','2','3','4','5','6','7','8','9']))
                   
for tens in allpossible:
    digits = convertTuple(tens)
    numbers.append(digits)


for x in numbers:
    if int(x[0:10]) % 10 == 0:
        if int(x[0:9]) % 9 == 0:
            if int(x[0:8]) % 8 == 0:
                if int(x[0:7]) % 7 == 0:
                    if int(x[0:6]) % 6 == 0:
                        if int(x[0:5]) % 5 == 0:
                            if int(x[0:4]) % 4 == 0:
                                if int(x[0:3]) % 3 == 0:
                                    if int(x[0:2]) % 2 == 0:
                                        Result = x
print(Result)
Answer = int(int(Result) * 1.7e-7 )                                        

print (Answer)

# answer =648
