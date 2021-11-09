
def checkequal(a):
    for i in range(0,3):
        if a[i]!=a[i+1]: return False
    return True
while (1):
    a = [int(i) for i in input().split()]
    check =False
    for i in a:
        if (i!=0):
            check =True
            break
    if (check == False): break
    count = 0
    while (checkequal(a)==False):
        t = a[0]
        for i in range(0,3):
            a[i]=abs(a[i]-a[i+1])
        a[3]=abs(a[3]-t)
        count+=1
    print(count)

