import math

def isPrime(s):
    if (s<2): return False
    for i in range(2,int(math.sqrt(s))+1):
        if (s%i==0): return False
    return True

t = int(input())
while (t>0):
    t-=1
    a= input()
    s = 0
    for i in a:
        s+=int(i)
    if (isPrime(s)==False): print('NO')
    else: print('YES')