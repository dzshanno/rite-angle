from itertools import permutations
import triangles
import operator

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
list_of_triangles = [test for test in  threesides if triangles.is_triangle([test[0],test[1],test[2]])]

#loop through all triangles
for testcase in list_of_triangles:
    sides = [testcase[0],testcase[1],testcase[2]]
    testarea = triangles.area(sides)
    testcase[3] = testarea    

smallest = min(list_of_triangles, key=operator.itemgetter(3))
largest = max(list_of_triangles, key=operator.itemgetter(3))

# print output  
print(f"largest {largest}")
print(f"smallest {smallest}")
