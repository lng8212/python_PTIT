a = str(input())
vh,vt = 0,0
for i in a:
    if(i.islower()==True): vt+=1
    elif(i.isupper()==True): vh+=1
if(vt>=vh): print(a.lower())
else: print(a.upper())