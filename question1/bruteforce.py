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


import math
import itertools



# Create list of possible triangles
allpossible = list(itertools.permutations(['0','1','1','1','1','1','1','2','2','2','2','2','2','2','2','2','2','2','2','3','3','3','3','3','3','3','3'],3))
total_solutions = len(allpossible)
four_black_solutions = 0
for choices in allpossible:
    black = int(choices[0])+int(choices[1])+int(choices[2])
    if black == 4:
        four_black_solutions = four_black_solutions + 1


prob_of_4_black = four_black_solutions / total_solutions

prob_of_4_black_to_3sf = round(prob_of_4_black, 3 - int(math.floor(math.log10(abs(prob_of_4_black)))) - 1)
Answer = int(prob_of_4_black_to_3sf * 185)
print(Answer)