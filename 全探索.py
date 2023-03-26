n,x=map(int,input().split())

result=0

#計算量を減らすためにforループを一つ落とす

for a in range(1,n+1):
  for b in range(a+1,n+1):
    if b<x-a-b<=n:
      result+=1
      break


print(result)

"""
NP完全

"""
    
