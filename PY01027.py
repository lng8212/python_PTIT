a = input()
check = False
for i in a:
    if (i!='6' and i!='8'):
        check = True
        break
if (check == True): print('NO')
elif a[0]=='8': print('NO')
else:
    
    for i in range (1, len(a)-2):
        if (a[i]=='8' and a[i+1]=='8' and a[i+2]=='8'):
            check =True
            print('NO')
            break
    if (check == False): print('YES')