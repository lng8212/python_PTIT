n = int(input())
a = list()
while (len(a)<n):
    b = list(map(int, input().split()))
    for i in b:
        a.append(i)

evenN= list()
oddN = list()
posEven = list()
posOdd = list()
for i in range(len(a)):
    if (a[i]%2==0):
        evenN.append(a[i])
        posEven.append(i)
    else: 
        oddN.append(a[i])
        posOdd.append(i)
for i in range(0, len(evenN)-1):
    for j in range(i+1,len(evenN)):
        if (evenN[i]>evenN[j]):
            evenN[i],evenN[j] = evenN[j],evenN[i]
            # posEven[i],posEven[j] = posEven[j],posEven[i]
for i in range(0,len(oddN)-1):
    for j in range(i+1,len(oddN)):
        if (oddN[i]<oddN[j]):
            oddN[i], oddN[j] = oddN[j], oddN[i]
            # posOdd[i], posOdd[j]= posOdd[j], posOdd[i]
for i in range(len(oddN)):
    a[posOdd[i]]= oddN[i]
for i in range(len(evenN)):
    a[posEven[i]] = evenN[i]

for i in a:
    print (i, end = ' ')
