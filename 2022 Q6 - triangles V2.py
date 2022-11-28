from itertools import permutations
import math

# Function definition to check given sides make a non zero area triangle
def is_triangle(sides):
    a,b,c=sides
    if a+b>c and b+c>a and c+a>b:
        return True
    else:
        return False


# Create list of possible triangles
allpossible = list(permutations(['1','2','3','4','5','6','7','8','9']))
#combine into 3 triple digit tuples with no common digits
threesides = []
for possible in allpossible:
    first = int(possible[0]+possible[1]+possible[2])
    second = int(possible[3]+possible[4]+possible[5])
    third = int(possible[6]+possible[7]+possible[8])
    threesides.append([first,second,third]) 
    
#create a list of just those threesides that make legitimate tringles with non-zero area
triangles = [test for test in  threesides if is_triangle(test)]

# define the largest and smallest area found
largest = [0,['','','']]
smallest = [float('inf'),['','','']]

# Function definition to return the area of a triangle given the 3 sides - can be zero
def area (sides):
    a,b,c = sides
    try:
        s = (a + b + c) / 2
        Area = math.sqrt((s*(s-a)*(s-b)*(s-c)))
        return Area 
    except:
        return 'Undefined' 


#loop through all triangles
for testcase in triangles:
    
    testarea = area(testcase)
        
    if testarea > largest[0]:
        largest = testarea, testcase
    if testarea < smallest[0]:
        smallest = testarea, testcase
        
print(largest)
print(smallest)
