n = int(input())

a = []

for i in range(n):
    b = list(map(int,input().split()))
    a.append(b)


if (n==2):
    print(n//2,n//2)
else:
    sum1 = 0
    sum2 = 0

    for i in range (n):
        if(i!=n-1):
            if(i>0): sum2 += a[i][i+1]
            sum1 += a[i][i+1]
        else:
            sum1 +=a[n-1][0]
            sum2+=a[n-1][1]
    

    kq = []
    kq.append((sum1-sum2)//2)

    for i in range(1,n):
        kq.append(a[i-1][i]-kq[i-1])
    for i in kq:
        print(i, end = " ")