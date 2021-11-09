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
    l = len(a)-1
    s = int(a[l-3])*1000+int(a[l-2])*100+int(a[l-1])*10+int(a[l])
    if (isPrime(s)== False): print('NO')
    else: print('YES')