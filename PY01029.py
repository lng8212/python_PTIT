import math

def reverseNum(n):
    s = 0 
    while (n>0):
        s=s*10+n%10
        n = int(n/10)
    return s

t = int(input())
while (t>0):
    t-=1
    a = int(input())
    b = reverseNum(a)
    if (math.gcd(a,b)==1): print('YES')
    else: print('NO')