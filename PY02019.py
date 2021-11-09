import math



n = int(input())
ar = [int(i) for i in input().split()]
ar.sort()
for i in range(len(ar)-1):
    for j in range(i+1,len(ar)):
        if(math.gcd(int(ar[i]),int(ar[j]))==1): print(ar[i],ar[j])