n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
unique_a = list()
unique_b = list()
for i in a:
    if (i not in unique_a):
        unique_a.append(i)
for i in b:
    if(i not in unique_b):
        unique_b.append(i)
unique_a.sort()
unique_b.sort()
for i in unique_a:
    if (i in unique_b):
        print(i, end = ' ')
print()
for i in unique_a:
    if (i not in unique_b):
        print(i,end =' ' )
print()
for i in unique_b:
    if (i not in unique_a):
        print(i,end =' ')
print()
