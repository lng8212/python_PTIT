n = int(input())

a = [int(i) for i in input().split()]
s = 0
for i in range (0,len(a)-1):
    if (a[i]!= a[i+1]): s+=1

print(s)