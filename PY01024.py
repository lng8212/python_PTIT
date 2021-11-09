z = int(input())
while(z>0):
    z = z-1
    a = str(input())
    s = 0
    mark = False
    for i in range(0,len(a)-1):
        s += int(a[i])
        if (abs(int(a[i+1])-int(a[i]))!=2) :
            print('NO')
            mark = True
            break;
    s+=int (a[len(a)-1])
    if (mark==False):
        if(s%10==0): print('YES')
        else: print('NO')
    
