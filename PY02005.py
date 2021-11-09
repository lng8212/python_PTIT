n = int(input())
a = [int(i) for i in input().split()]
s = 0
for i in range (0,n-1):
    for j in range (i+1,n):
        if (a[i]>a[j]): 
            s+=1

print(s)