a = input()
b = []
for i in range(0,len(a),2):
    if(i+1<len(a)) : 
        tmp = a[i]+ a[i+1]
        b.append(int(tmp))

t = set(b)
for i in (sorted(t)):
    print(i, end = " ")