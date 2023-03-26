N,X=map(int,input().split())

A=list(map(int,input().split()))

def sol(A):

  for i in A:
      if X==i:
         print("Yes")
         return
  print("No")
  return

sol(A)