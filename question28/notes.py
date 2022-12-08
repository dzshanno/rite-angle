import math

for k in range(2,9):
    
    cosa = (math.sqrt(k)-1)/2
    a = math.acos(cosa)
    answer = math.sin(a)
    print (k, answer)
