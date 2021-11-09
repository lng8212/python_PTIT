a = str(input())
array = ['000','001','010','011','100','101','110','111']
mark = len(a)-1
ans =''
for i in range(len(a)-1,1,-3):
    mark = i
    arrayx = a[i-2]+a[i-1]+a[i]
    # print(array[i-2])
    for j in range(8):
        if (arrayx == array[j]): ans = ans + str(j)
mark -=3
if (mark>=0):
    fr=''
    for i in range(0,mark+1):
        fr +=a[i]
    while (len(fr)<3): fr = '0'+fr
    for j in range(8):
        if (fr == array[j]): 
            print(str(j),end='')
            break
for i in range(len(ans)-1,-1,-1):
    print(ans[i],end='')