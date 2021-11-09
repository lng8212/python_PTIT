t = int(input())
while (t > 0):
    t -= 1
    a = list(input())
    mem = 0
    for i in range(len(a)-1, 0, -1):
        if(int(a[i]) >= 5):
            a[i] = '0'
            x = int(a[i-1])+1
            a[i-1] = str(x)
        elif (int(a[i]) >= 1):
            a[i] = '0'
    st = "".join(a)
    num = int(st)
    print(num)
