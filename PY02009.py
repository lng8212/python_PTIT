t = int(input())
while (t>0):
    t-=1
    n = int(input())
    fre = {}
    s = 0
    ts = 0
    while (n>0):
        n-=1
        x = int(input())
        if (x in fre):
            fre[x]+=1
        else: fre[x]=1
    for i in fre:
        if(fre[i]>=ts):
            if(fre[i]>ts):
                s = i
                ts = fre[i]
            else:
                if (s>i):
                    s = i
                    ts= fre[i]
            
    print(s)


