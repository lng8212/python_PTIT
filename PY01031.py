t = int(input())
ar = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
while (t>0):
    t-=1
    a,b = map(int,input().split())
    ans = ''
    while (a>0):
        ans += ar[a%b]
        a = int(a/b)
    
    for i in range (len(ans)-1,-1,-1):
        print(ans[i], end = '')
    print()
