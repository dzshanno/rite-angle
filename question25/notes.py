#question 25
import sympy 
answers = []
for a in range (1000):
    for b in range (a):
        d=str(int(a+b))
        e=str(int(a-b))
        c=int(e+d)
        if c>10000 and sympy.isprime(c):
            answers.append(c)

print(min(answers))
            
        
        
    
        