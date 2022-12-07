from itertools import permutations
import operator
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


# Create list of possible triangles
allpossible = list(permutations(['1','2','3','4','5','6','7','8','9']))
#combine into a 3 triple digit tuple with no common digits
threesides = []
for possible in allpossible:
    first = int(possible[0]+possible[1]+possible[2])
    second = int(possible[3]+possible[4]+possible[5])
    third = int(possible[6]+possible[7]+possible[8])
    threesides.append([first,second,third,0]) 
    
#create a list of just those threesides that make legitimate tringles with non-zero area
list_of_triangles = [test for test in  threesides if is_triangle([test[0],test[1],test[2]])]

#loop through all triangles
for testcase in list_of_triangles:
    sides = [testcase[0],testcase[1],testcase[2]]
    testarea = area(sides)
    testcase[3] = testarea    

smallest = min(list_of_triangles, key=operator.itemgetter(3))
largest = max(list_of_triangles, key=operator.itemgetter(3))

# print output  
print(f"largest {largest}")
print(f"smallest {smallest}")
answer = int(largest[3]/smallest[3])
result = int(answer * 0.081)
print (answer)
print (result)

#result = 8
