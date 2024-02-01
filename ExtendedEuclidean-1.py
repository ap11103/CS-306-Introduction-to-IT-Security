#Alisha Patel
#I pledge my honor that I have abided by the Stevens Honor System.
#Extended euclidean algorithm to find the inverse of an integer b(mod a)

      

x = 0
y = 1

def extendedeuclidgcd(a,b):
   global x, y

   if(a == 0):
       x = 0
       y = 1
       return b
   else:
       gcd = extendedeuclidgcd(b%a, a)
       c = x
       d = y
       x = d - (b//a)*c
       y = c
       return gcd

def invmod(a, m):
    g = extendedeuclidgcd(a,m)
    if (g != 1):
        print("Inverse mod doesn't exist")
    else:
        final = (x%m + m)%m
        print("The inverse mod of the integer is ", final)



invmod(18,53)
invmod(25,47)
invmod(3, 17)
