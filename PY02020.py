n = int(input())
a = list(map(float, input().split()))
maxz = -1
minz = 11
for i in a:
    if (i>maxz): maxz = i
    if (i<minz): minz = i
b = []
for i in range(0,len(a)):
    if (a[i]!=maxz and a[i]!=minz):
        b.append(a[i])
avg = 0

for i in b:
    avg+=i
print(format(avg/len(b),'.2f'))