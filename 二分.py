li=[1,3,7,12,14,18,35,74]

tgt=7

right=len(li)
left=0

while right-left>1:
    mid=(right+left)//2
    if li[mid]>tgt:
        right=mid

    elif li[mid]<tgt:
        left=mid

    else:
        print(mid)
        break
