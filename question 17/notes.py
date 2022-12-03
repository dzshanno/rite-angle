# The triangle with sides root a, root b, root c exists and has area A.

# The point a,b,c lies on a sphere, centre the origin, with radius root 899 .

# The cuboid with sides a,b,c and  has surface area 1702

# What (to 3 s.f.) is A?

# To get your final answer, multiply this by  and take the integer part.

# a ** 2 + b**2 + c**2 = 899

# 2*a*b + 2*a*c + 2*b*c = 1702

# using s=(A+B+C)/2
# Area of triangle = math.sqrt(s*(s-a)*(s-b)*(s-c))
# A ** 2 = (ra+rb+rc)/2 * (rb+rc-ra)/2 * (ra+rc-rb)/2 * (ra+rb-rc)/2
# multiply out the above and multiply by 16
# 16 * A**2 = [(b+c-a)+(2*rb*rc)]*[(a-b-c)+(2*rb*rc)]
# which is in the form [x-y]*[x+y] = x**2 - y**2
# 16 A ** 2 = 4bc - (a-b-c)**2
# expand the brackets
# 16 A **2 = 4bc - [a**2+b**2+c**2 - 2ab - 2ac + 2bc]
# 16 A **2 = -[a2 + b2 + c2] + [2ab + 2bc + 2ac]
# 16 A**2 = 1702 - 899

import math

def set_sig_fig(answer,sigfig):
    result = round(answer, sigfig - int(math.floor(math.log10(abs(answer)))) - 1)
    return result

Area = math.sqrt((1702-899)/16)
print(Area)
Result = set_sig_fig(Area,3)
print(Result)
Answer = int(Result*1.8)
print(Answer)

#Answer = 12
