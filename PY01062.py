import math

t = int(input())
def isPrime(n):
    if (n<2): return False
    for i in range(2, int(math.sqrt(n))+1):
        if (n%i==0): return False
    return True


while (t>0):
    t-=1
    a = input()
    l = len(a)
    nonPrime = 0
    Prime = 0
    for i in range(0,l):
        if (isPrime(int(a[i]))==True): Prime+=1
        else: nonPrime+=1
    if (isPrime(len(a))==True and Prime>nonPrime): print('YES')
    else: print('NO')
