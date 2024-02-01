#Alisha Patel
#I pledge my honor that I have abided by the Stevens Honor System.
#Baby-Step Giant-Step Discrete Logarithm Problem

from math import sqrt, ceil


def dlog(b,g,p):
    #g^x = b(modp)
    #m = rounding up the sqrt of p
    m = ceil(sqrt(p-1))

    #creating a table for g^j for each value
    list1 = {pow(g,j,p): j for j in range(m)}

    #g^(-m)
    c = pow(g, m*(p-2),p)

    #creating the table for b(g^(-m))^i
    for i in range(m):
        y = (b* pow(c,i,p))%p
        #if there is a value that is also in the previous table
        #return the x value, x = m*i + j 
        if y in list1:
            return i*m + list1[y]

    #if there's no value in common -> return none
    return None

print(dlog(17,2,19))
print(dlog(14,2,19))

        

    
    
