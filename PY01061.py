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
    s = int(a[l-3])*100+int(a[l-2])*10+int(a[l-1])
    fr = int(a[0])*100 + int(a[1])*10 + int(a[2])
    if (isPrime(s)== True and isPrime(fr)== True): print('YES')
    else: print('NO')