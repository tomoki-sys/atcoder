"""
隣接リスト
隣接行列

UnionFind木

https://www.youtube.com/watch?v=oLO7kLNJt7A
むずい


"""

class UnionFind:
    def __init__(self,n:int):
        self.parent=[-1]*n

    def find(self,x):
        if self.parent[x]==-1:
          return x
        
        return self.find(self.parent[x])
    
    def union(self,x,y):
        x=self.find(x)#再帰で親に辿っている
        y=self.find(y)

        if x==y:
            return
        
        self.parent[x]=y#xの親はy


n,q=map(int,input().split())

uf=UnionFind(n)

for _ in range(q):
    p,a,b=map(int,input().split())
    a-=1
    b-=1


    if p==0:
        uf.union()

    if p==1:
        if uf.find(a)==uf.find(b):
            print("Yes")

        else:
            print("No")
            
            
