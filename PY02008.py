import math
def isPrime(a):
    if (a<2): return False
    for i in range(2, int(math.sqrt(a))+1):
        if (a%i==0): return False
    return True

ar= []


for i in range(2,8000):
    if (isPrime(i)==True): ar.append(i)

a,b = map(int,input().split())
print (b,end =' ')

z=b
for i in range (0,a):
    z = z + ar[i]
    print(z,end=' ')