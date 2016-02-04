import re
import cmath
from decimal import *


def get_prime_number(input):
    n = input[0]
    prime = 4
    
    if n <= 0:
        return "input error"
    if n == 1 or n == 2 or n == 3:
        return n

    while(True): 
        isPrime = True
        if n < 5:
            return prime  
        else:
            prime += 1     
        for i in range(2, prime):
            if prime % i == 0:
               isPrime = False
        if isPrime:
            n -= 1       
 
def valid_phone_number(input):
       number = input
       if re.match(r'^\d{3}-\d{3}-\d{4}$', number):
           return 'valid'
       else:
           return 'invalid'  

def pi(n):
    getcontext().prec = n
    pi = Decimal(0)
    k = 0
    nValue = "3."
    while k < n * 2:
        pi += (Decimal(1)/(16**k))*((Decimal(4)/(8*k+1))-(Decimal(2)/(8*k+4))-(Decimal(1)/(8*k+5))-(Decimal(1)/(8*k+6)))
        k += 1
    return str(pi)
    


def solve_quadratic(threeInputs):
    a = threeInputs[0]
    b = threeInputs[1]
    c = threeInputs[2]

    d = (b**2) - (4*a*c)

    ans1 = (-b-cmath.sqrt(d))/(2*a)
    ans2 = (-b+cmath.sqrt(d))/(2*a)

    return '{0} and {1}'.format(ans1, ans2)


def highest_common_factor(input):
    x = int(input[0])
    y = int(input[1])
    print x
    print y
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1,smaller + 1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i

    return hcf

def set_ops(set1, set2, operation):
    

    if not isinstance(set1, set) or not isinstance(set2, set):
        return "please input two lists"
    
    if operation == "union":
        return 'answer: {0}'.format(set1 | set2)
    elif operation == "intersection":
        return 'answer: {0}'.format(set1 & set2)
    elif operation == "difference":
        return 'answer: {0}'.format(set1 - set2)
    else:
        return "invalid operation"

