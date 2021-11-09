n = int(input())
a = []
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
k = int(input())
tren = 0
duoi = 0

for i in range(n):
    for j in range(len(a[i])):
        if (j>i): tren+=a[i][j]
        elif (j<i): duoi+=a[i][j]


if (abs(tren-duoi)<=k):
    print("YES")
    
else:
    print("NO")

print(abs(tren-duoi))
