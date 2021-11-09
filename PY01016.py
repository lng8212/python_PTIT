n = int(input())
while (n>0):
    n-=1
    a = str(input())
    for i in range(len(a)):
        if(a[i]>='0' and a[i]<='9'):
            x = int(a[i])
            for j in range (0,x):
                print(a[i-1],end ='')

    print('\n')
    
        