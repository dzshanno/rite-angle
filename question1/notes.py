#Question 1 - Stage 1
#A  3 cm by  3cm by  3cm cube of white wood is painted black all over, and then chopped into  27 cubes, each   1cm by  1cm by 1cm .

#These smaller cubes are then put into a bag and three are picked (without replacement) at random.

#What (to 3 s.f.) is the probability of getting exactly four black faces in total?

# To get your final answer, multiply this by  185 and take the integer part.

# 1 x centre = 0 black faces
# 6 x face = 1 black face
# 12 x edge = 2 black faces
# 8 x Korners = 3 black faces

# how many ways give 4 black

# KFC = 8/27 x 7/26 x 1/25
# EEC = 12/27 x 11/26 x 1/25
# EFF = 12/27 x 6/26 x 5/25

# total number of 
import math

KFC = (8/27)*(7/26)*(1/25)
# with 6 possible ways

EEC = (12/27)*(11/26) * (1/25)


EFF = (12/27) * (6/26) * (5/25)

total =  (6*KFC)+(3*EEC)+(3*EFF)

significant_digits = 3
rounded_total =  round(total, significant_digits - int(math.floor(math.log10(abs(total)))) - 1)

Answer = rounded_total * 185

print (Answer)

# Total = 0.031225071225071226
# to 3 s.f. = 0.0312
# answer = 5.771999999999999
# integer answer