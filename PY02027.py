import re

ans = list()
n = int(input())
while (n>0):
    n-=1
    a = input()
    x = re.findall(r'\d+', a)
    for i in x:
        ans.append(int(i))
ans.sort()
for i in ans:
    print(i)