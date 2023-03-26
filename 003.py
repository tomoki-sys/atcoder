"""
木
直径を求める
dfsをする→ある根っこからの最大の距離がわかる

"""
import sys
sys.setrecursionlimit(10**6)

n=int(input())

edges=[[] for _ in range(n)]

for _ in range(n-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    edges[a].append(b)
    edges[b].append(a)

dist=[0]*n

def dfs(x,last=-1):
    global dist
    for to in edges[x]:
        if to==last:
            continue
        
        dist[to]=dist[x]+1
        dfs(to,x)

dfs(0)
    
    
