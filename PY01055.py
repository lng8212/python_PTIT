t = int(input())
def check(a):
    if (len(a)%2==0): return False
    if(a[0]==a[1]): return False
    x = a[0]
    for i in range(2,len(a),2):
        if (a[i]!=x): return False
    return True


while (t>0):
    t-=1
    a = input()
    if (check(a)== False): print('NO')
    else: print('YES')
