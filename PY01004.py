
import math

def isPrime(s):
    if (s<2): return False
    for i in range(2,int(math.sqrt(s))+1):
        if (s%i==0): return False
    return True



t = int(input())
while (t>0):
    t-=1
    n = int(input())
    s = 0
    for i in range (n):
        if(math.gcd(i,n)==1): s+=1
    if(isPrime(s)==True): print('YES')
    else: print('NO')

    

