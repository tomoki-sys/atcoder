
"""
幅優先探索
#https://www.youtube.com/watch?v=4sKzFGWoNYQ&list=PLwlP26Z1O_DesFumSto6rfa9T2jmk9iD4&index=3

重み向きなしのグラフ問題


"""
#%%
#https://www.youtube.com/watch?v=-meNDDzhfm0
#8:00
from collections import deque

class Solution:
    def numIslands(self,grid)->int:
        if grid==[]:
            return 0
        
        rows,cols=len(grid),len(grid[0])#マップの行列の長さを知る
        visited=set()#setは集合で、中に入っているかを確認するのに便利
        count=0

        def bfs(r,c):
            q=deque()
            
            directons=[(1,0),(-1,0),(0,1),(0,-1)]

            q.append((r,c))
            
            while q:
                row,col=q.popleft()#popに変えるだけで深さ優先探索になる
                for dir_r,dir_c in directons:
                    adj_r,adj_c=row+dir_r,col+dir_c

                    if (adj_r in range(rows)) and (adj_c in range(cols)) and (grid[adj_r][adj_c]==1) and ((adj_r,adj_c) not in visited):
                        q.append((adj_r,adj_c))
                        visited.add((adj_r,adj_c))#セットはappendではなく、setで追加する


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    bfs(r,c)#幅優先探索をしてカウントする
                    #陸とされるものを全て把握する
                    #隣接する１を全て取得する
                    count+=1

        return count
    
#%%
#https://www.youtube.com/watch?v=6QKW-HQV-hE
#計算量を減らすよりは実装方法
#迷路
#必ず最短距離が見つかるが、メモリを消費する
"""
キューをつかうFIFO"

"""


#%%

r,c=map(int,input().split())

sy,sx=map(int,input().split())

gy,gx=map(int,input().split())

grid=[list(input()) for _ in range(r)]


#grid=[]
#for i in range(r):
      #grid.append(list(input()))"""
  




print(grid)



        
# %%
print(1)
# %%
