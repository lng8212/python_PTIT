import math

def isPrime(a):
    if a<2: return False
    for i in range (2,int(math.sqrt(a))+1):
        if (a%i==0): return False
    return True


R,C= map(int, input().split())

a = []
for i in range(R):
   a.append([int(j) for j in input().split()])

for i in range (R):
    for j in range (C):
        if (isPrime(a[i][j])==True): a[i][j]=1
        else: a[i][j]=0

for i in range(R):
    for j in range(C):
        print(a[i][j], end = ' ')
    print() 