li=[3,6,2,53,3,7,19,4,2,567,46,3,2,16,567,8,11,875,65,4,3,9,2,345,67,34,28]
#小ー大

for i in range(len(li)):
    for j in range(len(li)-1-i):
        if li[j]>li[j+1]:
            tmp=li[j]
            li[j]=li[j+1]
            li[j+1]=tmp

print(li)