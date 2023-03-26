
"""
# ##############
#     ##########
# ### ##########
# # #  #########
# ###       ####
# ######### ####
# ######### ####
# ### ##### ####
# ### ##### ####
# ###       ####
# ######### ####
# ### #####    #
# ###   ### ####
# ##### ### ####
#              #
################
(2,0)
(15,15)

"""

from collections import deque

q=deque()

row,col=map(int,input().split())

li=[list(input()) for _ in range(row)]


#インデックスに置き換え済み
s=[0,1]
g=[14,14]

x=[0,1,0,-1]
y=[1,0,-1,0]

q.append(s)

li[s[0]][s[1]]=1

while len(q)!=0:
    tmp=q.popleft()
    print(tmp[0])

    for i in range(4):

        if (tmp[0]+x[i]>=0 and tmp[0]+x[i]<=col-1) and (tmp[1]+y[i]>=0 and tmp[1]+y[i]<=row-1) and li[tmp[0]+x[i]][tmp[1]+y[i]]!="#":

            li[tmp[0]+x[i]][tmp[1]+y[i]]=int(li[tmp[0]][tmp[1]])+1

            if tmp[0]+x[i]==g[0] and tmp[1]+y[i]==g[1]:
                print(li[tmp[0]+x[i]][tmp[1]+y[i]])

            q.append(li[tmp[0]+x[i]][tmp[1]+y[i]])






    




# %%
