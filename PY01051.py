
from typing import SupportsRound


def sTN(s):
    if (s<10): return False
    x = s
    s1 = 0
    while (s>0):
        s1 = s1*10 + s%10
        s = int(s/10)
    if (x == s1):return True
    return False


t = int(input())
while (t>0):
    t-=1
    a= input()
    s = 0
    for i in a:
        s+=int(i)
    if (sTN(s)==False): print('NO')
    else: print('YES')