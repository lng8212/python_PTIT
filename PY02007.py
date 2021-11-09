
a = list()
while (len(a)<10):
    ar = input().split()
    for i in range (0, len(ar)):
        a.append(int(ar[i]))
fre=[]
for i in range(0,len(a)):
    a[i] = a[i]%42
s = 0
tmp = {}
for i in a:
    if (i in tmp):
        tmp[i]+=1
    else:
        tmp[i]=1
print(len(tmp))


