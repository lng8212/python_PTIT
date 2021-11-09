def greated (a,b):
    if (len(a)>len(b)): return a
    elif(len(b)>len(a)): return b
    else:
        for i in range(len(a)):
            if (int(a[i])>int(b[i])): return a
            elif (int(b[i])>int(a[i])): return b
            else: continue
    return a
def small(a,b):
    if (len(a)<len(b)): return a
    elif(len(b)<len(a)): return b
    else:
        for i in range(len(a)):
            if (int(a[i])<int(b[i])): return a
            elif (int(b[i])<int(a[i])): return b
            else: continue
    return a
def checkEqual(a):
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if (a[i]!=a[j]): return False
    return True

while (1):
    n = int(input())
    if (n==0): break
    a = list()
    for i in range(n):
        a.append(str(input()))
    for i in range( len(a)):
        while (a[i][0]=='0'):
            a[i]=a[i][1:]
    if (checkEqual(a) == True): print('BANG NHAU')
    else:
        maxz = a[0]
        minz = a[0]
        for i in range(1,len(a)):
            maxz = greated(a[i],maxz)
            minz = small(a[i],minz)
        print (minz,maxz)
    
    