from collections import deque


r,c=map(int,input().split())

sy,sx=map(int,input().split())
sy-=1
sx-=1

gy,gx=map(int,input().split())

gy-=1
gx-=1

grid=[list(input()) for _ in range(r)]

q=deque()

q.append((sy,sx))

dist=[[-1 for _ in range(c)] for _ in range(r)]

dist[sy][sx]=0 #探索済み


dy=(0,1,0,-1)
dx=(1,0,-1,0)


while(len(q)>0):
    now=q.popleft()
    y,x=now

    #４方位を調べる
    for  di in range(4):
        ny=y+dy[di]
        nx=x+dx[di]

        if(ny<0 or ny>=r or nx<0 or nx>=c):
            continue
        
        if(grid[ny][nx]=="#"):
          continue

        if(dist[ny][nx]!=-1):
            continue
        
        dist[ny][nx]=dist[y][x]+1

        q.append((ny,nx))

print(dist[gy][gx])



