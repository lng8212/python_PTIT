import math

t = int(input())
def isPrime(n):
    if (n<2): return False
    for i in range(2, int(math.sqrt(n))+1):
        if (n%i==0): return False
    return True


while (t>0):
    t-=1
    a = input()
    check = True
    for i in range(0,len(a)):
        if (isPrime(i)==True and isPrime(int(a[i]))==False):
            check = False
            break
        elif (isPrime(i)==False and isPrime(int(a[i]))==True):
            check =False
            break
    if (check == False): print('NO')
    else: print('YES')