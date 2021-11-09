t = int(input())
while (t>0):
    t-=1
    a,b = map(int, input().split())
    ans =0
    while (a>0):
        a = int (a/b)
        ans+=a
    print(ans)