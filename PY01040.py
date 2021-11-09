t = int(input())


ar = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
while (t>0):
    t-=1
    a = input()
    b = a[:int(len(a)/2)]
    a = a[int(len(a)/2):int(len(a))]
    sb = 0
    sa = 0
    c = []
    d = []
    for i in b:
        if (i in ar):
            sb+=ar.index(i)
    for i in range(len(b)):
        x = (ar.index(b[i])+sb)%26
        c.append(ar[x])
    for i in a:
        if (i in ar):
            sa+=ar.index(i)
    for i in range(len(a)):
        x = (ar.index(a[i])+sa)%26
        d.append(ar[x])
    ans = []
    for i in range(len(a)):
        vt = ar.index(d[i])
        x = (ar.index(c[i])+vt)%26
        ans.append(ar[x])
    
    for i in ans:
        print(i, end = "")
    print()