t = int(input())
while (t>0):
    t-=1
    a = input()
    s = 1
    for i in a:
        if (i=='0'): continue
        s = s * int(i)
    print(s)