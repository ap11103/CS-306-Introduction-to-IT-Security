#Alisha Patel
#I pledge my honor that I have abided by the Stevens Honor System.
#Find a random 32-bit Sophie Germain Prime Q and associated prime P = 2Q+1
#Find smallest integer g in Zp*
#Use P, Q, g to verify 

import random


limit = pow(2, 32) - 1
#efficiently works for smaller numbers, like 50
num = []

"""
isPrime determines if the given number is prime, which is used to determine
the sophie germain primes for a n and m.
Sophie creates a lists of all the sophie prime numbers and then initialize p and q
"""
def isPrime(n):
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return False
    return True

for n in range(2,limit):
    
    m = 2*n + 1
    if isPrime(n) and isPrime(m):
        num.append(n)

print(num)
Q = random.choice(num)
P = 2 * Q + 1
print(Q)
print(P)


'''
def gcd(a,b):
    if (a == 0):
        return b
    return gcd(b%a, a)

def subgroup(n):
    group = []
    group += [1]

    for i in range(2, n):
        if(gcd(i,n) == 1):
            group += [i]
    return group

order = subgroup(P)
'''

def generator(p):

    
    zp = []
    for n in range(1, p):
        zp += [n]
    for i in zp:
        for j in zp:
            if (i**j) % p == 1:
                if(p - 1)/i == Q:
                    return i
    return 0
    
'''
    zp = []
    for n in range(1, p):
        zp += [n]
    for i in zp:
        for j in zp:
            if (i**j) % p == 1:
                if(p - 1)/i == Q:
                    if (len(order)) == Q:
                        return i
    return 0
 '''       

g = generator(P)
print(g)

"""
The secret keys is the efficient method for computing modular exponentiation
"""

def secretkeys(a,b,c):
    var = 1
    if b == 1:
        var *= a % c
        return var
    elif (b % 2) == 0:
        return secretkeys(a, b/2, c)**2 % c
    else:
        return a*(secretkeys(a, (b-1)/2, c)**2) % c

"""
a and b are random numbers chose from Zp
calculate x = g^a mod P, y - g^b mod P
then after exchanging keys, compute l and k
through the bool function check whether it is true or false
"""

a = random.randint(1, Q)
b = random.randint(1, Q)

x = secretkeys(g, a, P)
y = secretkeys(g, b, P)

l = secretkeys(x, b, P)
k = secretkeys(y, a, P)

def bool(l, k):
    if l == k:
        result = True
    else:
        result = False
    return result

result = bool(l, k)
print(x)
print(y)
print(result)



"""
#dump to public.json

public_values = {"P" : p, "Q" : q, "g" : 0}

with open("public.json", "w") as jfile:
    json.dump(public_values, jfile)

#load to public.json
with open("public.json", "r") as jfile:
    public_values = json.load(jfile)

#find g here

public_values["g"] = g

with open("public.json", "w") as jfile:
    json.dump(public_values, jfile)

"""




