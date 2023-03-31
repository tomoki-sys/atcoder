H,W=map(int,input().split())

A=[list(map(int,input().split())) for _ in range(H)]

B=[[0]*W for _ in range(H) ]


#列に合計を全て足していく
#列の合計値を求める
#列に足す

for j in range(W):
  tmp=0
  for i in range(H):
      tmp+=A[i][j]
  for i in range(H):
      B[i][j]+=tmp


for j in range(H):
  tmp=0
  for i in range(W):
      tmp+=A[j][i]
  for i in range(W):
      B[j][i]+=tmp
      B[j][i]-=A[j][i]

  print(*B[j])




  
    