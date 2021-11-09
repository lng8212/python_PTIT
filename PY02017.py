t = int(input())
while (t>0):
    t-=1
    n = int(input())
    a = list (map(int, input().split()))
    fre = {}
    for i in a:
        if (i in fre):
            fre[i]+=1
        else:
            fre[i]=1
    for i in fre:
        if (fre[i]%2!=0):
            print(i)
            break