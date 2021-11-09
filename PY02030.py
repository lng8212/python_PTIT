import math

def isPrime(n):
    if (n<2): return False
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i==0): return False
    return True


def check(n,i):
    s = 0
    for vt in range(0,i+1):
        s+=n[vt]
    if (isPrime(s)==False): return False
    s = 0
    for vt in range(i+1,len(n)):
        s+=n[vt]
    if(isPrime(s)== False): return False
    return True




n = int(input())

a = list(map(int,input().split()))

b = {}
for i in a:
    if (i not in b):
        b[i]=1
    else:
        b[i]+=1

c = []
for i in b:
    if (b[i]>=1):
        c.append(i)
ktra= False
for i in range(len(c)):
    if(check(c,i)==True):
        ktra =True
        print(i)
        break
if (ktra == False ): print("NOT FOUND")