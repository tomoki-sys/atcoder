"""
for i in range(1<<n):0~2^n-1

for i in range(1<<n):
    for j in range(n):
      if i&(1<<j):
"""

n=int(input())
a=list(map(int,input().split()))

for i in range(1<<n):
    use=[False]*n

    for j in range(n):
        if i&(1<<j):
            use[j]=True

    total =0
    for j in range(n):
        if use[j]:
            total+=a[j]


         