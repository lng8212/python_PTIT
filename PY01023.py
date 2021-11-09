import math


t = int(input())
while (t>0):
    t-=1
    n = int(input())
    print ('1 ', end = '')
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i==0):
            s = 0
            while (n%i==0):
                n = int(n/i)
                s+=1
            print('* ' +str(i) + '^' +str(s), end = ' ')
    if (n>1): print('* ' + str(n) + '^1', end = '')
    print()
