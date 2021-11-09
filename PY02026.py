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
check= False
if (len(unique_a)!= len(unique_b)): check = True
else :
    for i in range (len(unique_a)):
        if (unique_a[i]!=unique_b[i]): 
            check =True
            break
if ( check == True): print('NO') 
else: print('YES')