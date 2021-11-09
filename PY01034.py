t = int(input())

while (t>0):
    t-=1
    a = input()
    b = []
    for i in a:
        b.append(i)
    if(len(b)==1): 
        print(-1)
        continue
    i = len(b)-2
    while(i>=0 and b[i]<=b[i+1]): i-=1
    if (i<0): print(-1)
    else:
        max = i +1
        for j in range(i+1,len(b)):
            if(b[j]<b[i] and b[j]>b[max]):
                max = j
        b[i],b[max] = b[max], b[i]
        if (b[0]=='0'): print (-1)
        else :
            for i in b:
                print(i,end = "")
            print()

   

