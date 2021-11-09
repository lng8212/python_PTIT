t = int(input())
while (t>0):
    t-=1
    n = int(input())
    a = input()
    b = input()
    arr1 = a.split()
    arr2 = b.split()
    lg = len(arr1)
    for i in range (0,lg):
        arr1[i]=int(arr1[i])   
        arr2[i]=int(arr2[i])
    arr1.sort()   
    arr2.sort()
    check = False
    for i in range (0,lg):
        if(arr1[i]>arr2[i]):
            check = True
            break
        
    if (check == False): print('YES')
    else: print('NO')
    
