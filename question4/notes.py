import math

# Question 4 - Stage 1
# The lines x= y, y=ax and y= bx+c
# where  b<a<0 and c>0
# enclose an equilateral triangle of area .
# What is the sum (to 3 s.f.) of the y-coordinates of the three vertices of the triangle?

# To get your final answer, multiply this by 476 and take the integer part.

# find coordinates of intersect points
# intersect of y = x and y=ax = (x1,y1) = (0,0)
# intersect of y=ax and y=bx+c = (x2,y2) = ([c/(a-b)],[ac/(a-b)])
# intersect of y=x and y=bx+c = (x3,y3) = ([c/(1-b)],[c/(1-b)])

# y=x and y=ax intersect at 60 degrees in order to form an eq triangle
# angle of y=x = arctan1 = 45 degrees
# angle of y=ax = -15 or -75

# y=x and y=bx+c intersect at 60 degrees in order to form an eq triangle
# 
# angle of y=bx+c = -15 or -75 degrees

# but b<a so 

d = -15
r = math.radians(d)
a = math.tan(r)
print('A is '+str(a))

d = -75
r = math.radians(d)
b = math.tan(r)
print('B is '+str(b))

                    
def Areagivencoords(x1,y1,x2,y2,x3,y3):
# Area = abs(0.5*((x1*(y2-y3))+(x2*(y3-y1))+(x3*(y1-y2))))
    
# given x1,y1 === 0
# for this question
    Area = abs(0.5*((x2*y3)-(x3*y2)))
    
# for this question area = 1
# x2*y3 - x3*y2 = 2



# (c/(a-b))*(c/(1-b)) - (c/(1-b))*(a/(a-b) *c) = 2
# c*c*[(1/(a-b)*1/(1-b))-(1/(1-b)*a(a-b))]=2

f = 1/(a-b)
g = 1/(1-b)

#  cf*cg - cg*caf = 2
# c*c*f*g - c*c*f*g*a = 2
# c*c*(f*g(1-a)=2
#
c = math.sqrt(abs(2/(f*g*(1-a))))
print('c is' + str(c))

result = (a*f*c)+(g*c)
print('result is' + str(result))

result_to_3sf = round(result, 3 - int(math.floor(math.log10(abs(result)))) - 1)
print(result_to_3sf)

Answer = int(result_to_3sf*476 )

print(Answer)
Answer = 324
