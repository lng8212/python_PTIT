z = int(input())
while(z>0):
    z = z-1
    string  = input()
    t = string[0]
    mark = True
    for i in string:
        if (i<t) : 
            print('NO')
            mark = False
            break
        t = i
    if (mark == True): print('YES') 
