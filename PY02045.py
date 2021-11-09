
n = input()
while (len(n)>1):
    k = len(n)
    a1 = n[:int(k/2)]
    a2 = n[int(k/2):]
    if (a1 == ''): x1 = 0
    else: x1 = int(a1)
    if (a2 ==''): x2 = 0
    else:x2 = int(a2)
    x3 = x1 + x2
    print(x3)
    n = str(x3)


    
    
        

