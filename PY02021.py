t = int(input())
while (t>0):
    t-=1
    n,m,o = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    a.sort()
    b.sort()
    c.sort()
    check =False
    i,j,k = 0,0,0
    while (i<n and j<m and k<o):
        if (a[i]==b[j] and a[i]==c[k]):
            print(a[i], end = ' ')
            check =True
            i+=1
            j+=1
            k+=1
        elif (a[i]<b[j]):
            i+=1
        elif (b[j]<c[k]):
            j+=1
        else: k+=1

    if (check==False): print('NO')
    else: print()