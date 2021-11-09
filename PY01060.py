t = int(input())

while (t>0):
    t-=1
    a= input()
    c = 0
    l = 1
    check = False
    for i in range(0, len(a)):
        if (i%2!=0): c+=int(a[i])
        elif (i%2==0):
            if (int(a[i])==0): continue
            else:
                l*=int(a[i])
                check =True
    if (check ==False): print(l,0)
    else: print(l,c)
        