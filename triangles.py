import math

# Function definition to check given sides make a non zero area triangle
def is_triangle(sides):
    a,b,c=sides
    if a+b>c and b+c>a and c+a>b:
        return True
    else:
        return False
    
    # Function definition to return the area of a triangle given the 3 sides - can be zero
def area (sides):
    a,b,c = sides
    try:
        s = (a + b + c) / 2
        Area = math.sqrt((s*(s-a)*(s-b)*(s-c)))
        return Area 
    except:
        return 'Undefined' 
