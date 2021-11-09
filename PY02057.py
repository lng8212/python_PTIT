
n,m = map(int,input().split())
a = []
for i in range(n):
    b = list(map(int,input().split()))
    a.append(b)

minz = 999999
maxz = -1
for i in range(n):
    for j in range(len(a[i])):
        if (a[i][j]>maxz): maxz = a[i][j]
        if (a[i][j]<minz): minz = a[i][j]
check = False

for i in range(n):
    for j in range(len(a[i])):
        if (a[i][j] == maxz - minz):
            if (check == False): print(maxz - minz)
            check =True
            print("Vi tri [" + str(i) + '][' + str(j) +']' )
if (check == False):print("NOT FOUND")

