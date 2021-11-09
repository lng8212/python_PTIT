def sumN(n):
    s = 0
    while (n>0):
        s = s+n%10
        n = int(n/10)
    return s

t = int(input())
while (t>0):
    t-=1
    n = int(input())
    a = list(map(int,input().split()))
    b = list()
    for i in a:
        b.append(sumN(i))
    
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if (b[i]>=b[j]):
                if (b[i]==b[j]):
                    if (a[i]>a[j]): 
                        b[i],b[j]= b[j],b[i]
                        a[i],a[j] = a[j], a[i]
                else:
                    b[i],b[j]= b[j],b[i]
                    a[i],a[j] = a[j], a[i]
    for i in a:
        print (i,end = ' ')
    print()



