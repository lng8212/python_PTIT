n = int(input())
a = list(map(int,input().split()))
a.sort()
num = a[0]
check = False
if (a[0]>1): print(1)
else:
    for i in a:
        if (i == num ): continue
        if (i-num ==1):
            num = i
            continue
        if (i-num>1):
            num = num+1
            check = True
            break
    if (check == True): print(num)
    else: print(a[len(a)-1]+1) 
    

