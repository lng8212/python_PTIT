n = int(input())
while (n>0):
    n-=1
    string = input()
    string = string.split()
    x = string[0]
    y = string[1]
    x = int(x)
    y = int(y)
    a=[]
    a.append(1)
    a.append(1)
    for i in range(2,93):
        a.append(a[i-1]+a[i-2])
    for i in range(x-1,y):
        print(a[i],end = ' ')
    print('')