from typing import Counter


t = int(input())
while (t>0):
    t-=1
    n = int(input())
    a = input()
    b = a.split()
    maxz = 0
    ans = b[0]
    for i in range (len(b)):
        b[i]=int(b[i])        
    c = Counter(b)
    if (c.most_common(1)[0][1]>n/2): print(c.most_common(1)[0][0])
    else: print('NO')
