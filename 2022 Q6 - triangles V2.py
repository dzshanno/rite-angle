from itertools import permutations
import triangles

# Create list of possible triangles
allpossible = list(permutations(['1','2','3','4','5','6','7','8','9']))
#combine into a 3 triple digit tuple with no common digits
threesides = []
for possible in allpossible:
    first = int(possible[0]+possible[1]+possible[2])
    second = int(possible[3]+possible[4]+possible[5])
    third = int(possible[6]+possible[7]+possible[8])
    threesides.append([first,second,third]) 
    
#create a list of just those threesides that make legitimate tringles with non-zero area
list_of_triangles = [test for test in  threesides if triangles.is_triangle(test)]

# define the largest and smallest area found
largest = [0,['','','']]
smallest = [float('inf'),['','','']]

#loop through all triangles
for testcase in list_of_triangles:
    
    testarea = triangles.area(testcase)
        
    if testarea > largest[0]:
        largest = testarea, testcase
    if testarea < smallest[0]:
        smallest = testarea, testcase
        
print(largest)
print(smallest)
