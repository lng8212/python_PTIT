n = int(input())
while (n>0):
    n-=1
    a = str(input())
    c = ''.join(reversed(a))
    check = False
    for i in range(1,len(a)):
        if(abs(ord(a[i])-ord(a[i-1]))!= abs(ord(c[i])-ord(c[i-1]))): 
            check = True
            break

    if (check == True): print('NO')
    else: print('YES')