
import math

n = int(input())

a = []
for i in range(n):
    b = list(map(int,input().split()))
    a.append(b)
k = int(input())
stren =0
sduoi = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        if (i+j<n-1): stren+=a[i][j]
        elif(i+j>n-1): sduoi+= a[i][j]
    
if (abs(stren - sduoi)<=k): print("YES")
else: print("NO")
print(abs(stren-sduoi))