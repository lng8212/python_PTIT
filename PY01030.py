a = ["www.zframez.com","www.wikipedia.org","www.asp.net","www.abcd.in"]

ans = []
for i in a:
    ans.append(i[i.rfind('.')+1:])
print(ans)
def myFunc(x):
  return x[1]

list_tuples = [('a',23),('b',37),('c',11), ('d',29)]
list_tuples.sort(key =myFunc)
print(list_tuples)