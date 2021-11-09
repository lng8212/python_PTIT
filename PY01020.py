
n = int(input())
while (n>0):
    n-=1
    a = str(input())
    if (a[len(a)-2] =='8' and a[len(a)-1]=='6'): print('YES')
    else: print('NO')
