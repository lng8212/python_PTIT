b=[]
b.append (0)
b.append(0)
for i in range (2,10006):
    b.append(1)
for i in range(2,10006):
    if (b[i]==1):
        for j in range(i*2,10006,i):
            b[j]=0

a = []
for i in range (10006):
    if (b[i]==1):
         a.append(i)
def findz(n):
    for i in range(len(a)):
        if (a[i]<n): continue
        if (a[i]>=n): return i
    return len(a)-1
n = int(input())

arrx = list(map(int,input().split()))
s = 0


for i in arrx:

    if(i<2):
        s+= (2-i)
    elif(i in a):
        continue
    else:
        t = findz(i)
        s = max(s, min(abs(a[t]-i), abs(a[t-1]-i)))

print(s)
   
