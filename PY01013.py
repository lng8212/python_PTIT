import math

def isPrime(a):
    if (a<2): return False
    for i in range(2,int(math.sqrt(a))+1):
        if (a%i==0): return False
    return True

t = int(input())
def numS(a):
    s =0
    while (a>0):
        s+=a%10
        a = int(a/10)
    return s
while (t>0):
    t-=1
    a,b = map(int, input().split())
    num = math.gcd(a,b)
    if (isPrime(numS(num))==True): print('YES')
    else: print('NO')

