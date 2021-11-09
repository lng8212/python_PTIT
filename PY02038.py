import itertools



n = int(input())
a = list()
for i in range(0,n):
    b = input()
    a.append(b)
ans =0
for i in range (len(a)):
    s = 0
    for j in range(len (a[i])):
        if (a[i][j]=='C'): s+=1
    if (s>=2): ans += int((s*(s-1))/2)

for i in range (len(a)):
    s = 0
    for j in range(len (a[i])):
        if (a[j][i]=='C'): s+=1
    if (s>=2): ans += int((s*(s-1))/2)

print(ans)