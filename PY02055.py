import math


def isPrime(n):
    if (n<2): return False
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i==0): return False
    return True



n,m = map(int,input().split())
a = []
for i in range(n):
    b = list(map(int,input().split()))
    a.append(b)

maxP = -1
for i in range(n):
    for j in range(len(a[i])):
        if ((a[i][j]>maxP) and isPrime(a[i][j])==True):
            maxP = a[i][j]


if maxP == -1: print("NOT FOUND")
else:
    print(maxP)


    for i in range(n):
        for j in range(len(a[i])):
            if (a[i][j]==maxP):
                print("Vi tri [" + str(i) + "]["+ str(j)+']')


