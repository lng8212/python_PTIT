n,m = map(int, input().split())

a = []
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)

boc = []
boh = []
x= n
y =m
if (n>m):
    for i in range(0,n,2):
        boh.append(i)
        x-=1
        if (x==m): break

if (m>n):
    for i in range(1,m,2):
        boc.append(i)
        y-=1
        if (y==n): break

for i in range(n):
    if(i not in boh):
        for j in range(m):   
            if (j not in boc): print (a[i][j], end = ' ')
        print()
        


