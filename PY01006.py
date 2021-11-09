z = int(input())
while(z>0):
    z = z-1
    string  = input()
    mark = True
    for i in string:
        if (i!='4' and i!='7') : 
            print('NO')
            mark = False
            break
    if (mark == True): print('YES') 
