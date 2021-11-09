a,K,N = map(int, input().split())


z = N-a
l = int(a/K)
r = int((a+z)/K)
num = l+1
if (l>=r): print(-1)
for i in range(l+1,r+1):
    print(K*num-a, end = ' ')
    num+=1