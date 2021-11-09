n = int(input())
while (n>0):
    n-=1
    a = str(input())
    s = 0
    a =''.join(sorted(a))
    for i in a:
        if (i>='0' and i<='9'):
            s+=int(i)
        else: print(i,end='')
    print(s)    