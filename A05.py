N,K=map(int,input().split())

res=0

for a in range(1,N+1):

    for b in range(1,N+1):
        if 1<=K-a-b and K-a-b<=N:
            res+=1

    


print(res)
            