n = int(input())
while(n>0):
    n-=1
    a = str(input())
    s =1
    for  i in range(0,len(a)):
        if (s>1):
            s-=1
            continue
        val = a[i]
        if (i<len(a)-1 and  a[i]==a[i+1]):
            while (i<len(a)-1 and a[i]==a[i+1]):
                i+=1
                s+=1
        if (i!=len(a)-1 ): print(str(s)+val,end = '')
        else:
            if (a[len(a)-1]==a[len(a)-2]): print(str(s)+val,end='')
            else: print(str(1)+a[len(a)-1],end='')
        
    print('')