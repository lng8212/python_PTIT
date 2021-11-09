import math
t = int(input())
def isPrime(a):
    n = 0
    for i in a:
        n+= int(i)
    if (n<2): return False
    for i in range(2, int(math.sqrt(n))+1):
        if (n%i==0): return False
    return True
def check(a):
    for i in range(0,len(a),2):
        if (int(a[i])%2!=0): return False
    for i in range(1,len(a),2):
        if (int(a[i])%2==0): return False
    if (isPrime(a)==True): return True
    return False

while (t>0):
    t-=1
    a = input()
    if (check(a)== False): print('NO')
    else: print('YES')
