t = int(input())
x =t
while (t>0):
    t-=1
    a = input()
    b = input()
    frez = {}
    freb = {}
    check = False
    for i in a:
        if (i in frez):
            frez[i]+=1
        else: frez[i]=1
    for i in b:
        if (i in freb):
            freb[i]+=1
        else: freb[i] = 1
    for i in frez:
        if ( i in freb and frez[i]==freb[i]): continue
        else:
            check = True
            break
    print('Test '+ str(x-t)+':', end = ' ' )
    if (check ==True): print('NO')
    else: print('YES')
