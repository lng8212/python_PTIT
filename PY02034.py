a = input()
b = []
for i in range(0,len(a),2):
    if(i+1<len(a)) : 
        tmp = a[i]+ a[i+1]
        b.append(int(tmp))


check = {}
for i in b:
    if (i not in check):
        check[i]=1
    else:
        check[i]+=1
for i in check:
    print(str(i) + " " + str(check[i]))