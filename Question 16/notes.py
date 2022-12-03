#Q16
#The points  A (a,a) and B (b,b), where a<0 and b>0 , lie on the curve y=px2 + bx + 4.

#The gradient of the curve at A is b, and the gradient of the curve at B is a.

#What is a2+b2?

#To get your final answer, multiply this by 1.21 and take the integer part.

#points lie on the line y=x
# dy/dx = 2px+q
p = -0.5
q= 2

a=-2
b=4

Result = (a**2)+(b**2)
Answer = int(Result*1.21)

print(Answer)
