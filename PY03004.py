import re


n = int(input())

b = {}

while (n>0):
    n-=1
    a = []
    a.extend(re.findall(r'\w+',input()))
    for i in a:
        if (i.lower() not in b):
            b[i.lower()]=-1
        else: b[i.lower()]-=1


c = sorted(b.items(),key = lambda x:(x[1],x[0]))
for i in c:
    print(i[0],str(0- int(i[1])))
