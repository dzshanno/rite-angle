import sympy
import math

def sum_of_digits (number):
    digits = [int(x) for x in str(number)]
    answer = sum(digits)
    return answer

def prod_of_digits (number):
    digits = [int(x) for x in str(number)]
    answer = math.prod(digits)
    return answer

primes = [2]

# make a list of primes
for i in range(5000):
    primes.append(sympy.nextprime(primes[-1]))
    

aprimes = [0]
mprimes = [0]
amprimes = [0]


for i in range(len(primes)):
    if (primes[i]+sum_of_digits(primes[i])) == sympy.nextprime(primes[i]):
        aprimes.append(primes[i])
    if (primes[i]+prod_of_digits(primes[i])) == sympy.nextprime(primes[i]):
        mprimes.append(primes[i])
    if (primes[i]+prod_of_digits(primes[i])+sum_of_digits(primes[i])) == sympy.nextprime(primes[i]):
        amprimes.append(primes[i])
    


   

print (aprimes)
print (mprimes)
print (amprimes)

for k in amprimes:
    if k not in aprimes:
        print (k)

