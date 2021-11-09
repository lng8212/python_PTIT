def lienTiep(n):
    countz = 0
    i = 1
    while (i*(i+1) < 2*n):
        a = float((float(n) - (i*(i+1))/2)/(i+1))
        if (a == int(a)):
            countz += 1
        i += 1
    return countz

t = int(input())
while (t>0):
    t-=1
    n = int(input())
    print(lienTiep(n))