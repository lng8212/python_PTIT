import math
def isPrime(a):
    if (a<2): return False
    for i in range(2, int(math.sqrt(a))+1):
        if (a%i==0): return False
    return True    


n = int(input())
a = list(map(int, input().split()))

for i in range(0,len(a)-1):
    for j in range (i+1,len(a)):
        if (isPrime(a[i]) and isPrime(a[j]) and a[i]>a[j]):
            a[i],a[j] = a[j], a[i]
for i in a:
    print(i,end = ' ')