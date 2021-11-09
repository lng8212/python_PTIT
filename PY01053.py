n = int(input())
while (n>0):
    n-=1
    a = input()
    s = 0
    for i in a:
        s+=int(i)
    if (s%3==0): print('YES')
    else: print('NO')