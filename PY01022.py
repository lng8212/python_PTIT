a= input()
s = 0
if (a[0]=='-'): s += ord('-') - ord('0')
else : s+=ord(a[0])- ord('0')
for i in range(1,len(a)):
    s+=ord(a[i])-ord('0')


buoc = 1
while (s>=10):
    buoc+=1
    s1 = s
    tmp = 0
    while (s1>0):
        tmp = tmp+s1%10
        s1 = int(s1/10)
    s=tmp
print(buoc)