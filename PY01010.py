n = int(input())
while (n>0):
    n-=1
    a = str(input())
    if ((a[0] == a[len(a)-2]) and (a[1]==a[len(a)-1])): print('YES')
    else: print('NO')