import math
from typing import Counter
def isPrime(a):
    if (a<2): return False
    for i in range(2, int(math.sqrt(a))+1):
        if (a%i==0): return False
    return True



n = int(input())


a = [int(i) for i in input().split()]

for i in range(0,len(a)):
    if(isPrime(a[i])==True):
        print(a[i], a.count(a[i]))
        for j in range(i+1,len(a)):
            if (a[j]==a[i]): a[j]=-1



