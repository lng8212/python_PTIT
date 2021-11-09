
while (1):
    n = int (input())
    if (n==0): break
    a = list()
    a.append(n)
    while (n>1):
        if (n%2==0):
            n= int(n/2)
            if (a.count(n) ==0): a.append(n)
        else:
            n= n*3 +1
            if (a.count(n) ==0): a.append(n)
    print(len(a))