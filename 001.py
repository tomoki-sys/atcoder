"""
minのmax
maxのmin→二分探索

長さl以上になるようになるように分ける時、ピースはK個以上に分けられる？に言い換える
余りにも気をつける
長さl以上になるようになるように分ける時、最大で何個に分けられるか

長さで二分探索する

https://atcoder.jp/contests/typical90/tasks/typical90_a

"""
N,L=map(int,input().split())
K=int(input())
A=[0]+list(map(int,input().split()))+[L]



def ok(l):
    left=0

    for i in range(K+1):#K回する＝K+１個に分ける
        right=left
        while right<len(A) and A[right]-A[left]<l:#切りたい長さになるまで右にずらしていく
            right+=1


        if right==len(A):
            return False
        
        left=right

    #上のループで一度もFalseにならずに無事に抜けられればTrueを返す
    return True

bottom,top=1,L+1

while top-bottom>1:
    mid=(top+bottom)//2
    if ok(mid):
        bottom=mid

    else:
        top=mid

print(bottom)
            
        


