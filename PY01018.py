P = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','_','.']
def swit(a,k):
    for i in range (0,len(P)):
        if (a==P[i]):
            x = (i+k)%28
            return P[x]


while (1):
    z= input().split()
    if (z[0]=='0'): break
    n = int(z[0])
    a = z[1]
    for i in range(len(a)-1,-1,-1):
      print(swit(a[i],n),end='')
    print('')