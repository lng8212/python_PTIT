a = input()
k = int(input())
b = []
for i in range(0,len(a),2):
    if(i+1<len(a)) : 
        tmp = a[i]+ a[i+1]
        b.append(int(tmp))


b.sort()
check = {}
for i in b:
    if (i not in check):
        check[i]=1
    else:
        check[i]+=1
ktra = False
for i in check:
    if(check[i]>=k):
        print(str(i) + " " + str(check[i]))
        ktra = True
if (ktra== False):
    print("NOT FOUND")