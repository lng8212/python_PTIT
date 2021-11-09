t = int (input())
while (t>0):
    t-=1
    a,b,c  = input().split()
    a = float(a)
    b = float (b)
    c = float (c)
    count = 0
    while (a<c):
        a = a + (a*b)/100
        count+=1
    print(count)
    