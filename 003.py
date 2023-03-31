"""
木
直径を求める
dfsをする→ある根っこからの距離が全てわかる
dfsは深さ優先探索
dfsはあくまでも全探索である。

直径→ある点から最も遠い点を選ぶ。その点から最も遠い点を結べば、それは直径になる。

最大の深さを求めるときは引数に現在の深さを入力して再帰のdfsを行うのがいい。
再帰＝枝を作るx。
再帰をfor文などで複数用いる事によって枝が生まれる。

隣接リスト
・インデックスが現在のノードの名前、要素がつながっている先にあるもの

改善
・隣接リストが何であるかがわかっていない
→リストはインデックスが何を表すか
→要素が何を表すかを認識する
→全てにも共通する
→コード一文が何を意味するかではなく、部品単位でモノを見る
→コードはあくまで接着剤であり、それ自体に意味はない。
→部分からではなく全体からものを見る
→パーツに分けていく

・再帰構造が何であるかがわかっていない
→for文と再帰を用いることで枝ができる
→一度再帰を用いることで、枝が伸びるイメージ


"""
import sys
sys.setrecursionlimit(10**6)
from collections import deque

n=int(input())

edges=[[] for _ in range(n)]

for _ in range(n-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    edges[a].append(b)
    edges[b].append(a)

dist=[0]*n



def dfs(x,last=-1):#xは現在のノード
    global dist
    for to in edges[x]:#現在のノードから行ける先がインデックスとして与えられている。
        if to==last:
            continue
        
        dist[to]=dist[x]+1
        dfs(to,x)

dfs(0)
max_dist=max(dist)
farest=dist.index(max_dist)

dist[farest]=0
dfs(farest)

print(max(dist)+1)
    
    
