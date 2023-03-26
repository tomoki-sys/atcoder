li=[3,6,2,53,3,7,19,4,2,567,46,3,2,16,567,8,11,875,65,4,3,9,2,345,67,34,28]
#小ー大



for i in range(len(li)-1):
    ind=i#最小値
    for j in range(i,len(li)):
        if li[ind]>li[j]:
            ind=j

        #インデックスだけわかればまあいい
            
    print(li)

        
    tmp=li[ind]
    li[ind]=li[i]
    li[i]=tmp

print(li)


        
        


