n, m = map(int, input().split())
a = list(map(int, input().split()))

b = {}
for i in a:
    if (i not in b):
        b[i] = 1
    else: b[i] += 1


sorted(b)
maxz = -1
for i in b:
    if (b[i] > maxz):

        maxz = b[i]

val = -1
maxz2 = -1
for i in b:
    if (b[i]>maxz2 and b[i]<maxz):
        maxz2 = b[i]
        val = i
if (val == -1): print("NONE")
else:
    for i in b: 
        if (b[i]==maxz2):
            if (i<val): val = i
    print(val)

