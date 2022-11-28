from itertools import permutations
import math

# Create list of possible triangles
possible = list(permutations(['1','2','3','4','5','6','7','8','9']))

results = [list(possibles)+['AREA'] for possibles in possible]
largest = [0,'','','']
smallest = [float('inf'),'','','']

# Function definition to return the area of a triangle given the 3 sides - can be zero
def area (a, b, c):
    try:
        s = (a + b + c) / 2
        Area = math.sqrt((s*(s-a)*(s-b)*(s-c)))
        return Area 
    except:
        return 'Undefined' 

# Function definition to check given sides make a non zero area triangle
def is_triangle(a,b,c):
    if a+b>c and b+c>a and c+a>b:
        return True
    else:
        return False

#loop through 
for testcase in results:
    first = int(str.join('',testcase[:3]))
    second = int(str.join('',testcase[3:6]))
    third = int(str.join('',testcase[6:9]))
    
    testarea = area(first,second,third)
    if testarea != 'Undefined' and testarea != 0:
        
        testcase[9] = testarea
        
        if testarea > largest[0]:
            largest = testarea, first, second, third
        if testarea < smallest[0]:
            smallest = testarea, first, second, third
        
print(largest)
print(smallest)



    