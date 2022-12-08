# question 19

import math

hourangle = 360/700
minangle = 360/100

# (360 * a/700) + 180 = (360 * a) / 100
# 180 = (360 * a)(1/100 - 1/700) 
a = (0.5)/(0.01 - (1/700))

print(a)

# by symmetry b = 100 - a

b=700 -a

print(b)

print(b-a)

answer = int((b-a)*0.247)

print (answer)
#answer =144

