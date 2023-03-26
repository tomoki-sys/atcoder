"""
動的計画法
ダイクストラ法
効率的に全探索を行う方法

足場iに来るためのコスト＝i-1からi or i-2からi

dp[i]=min(dp[i-1]+costi1,dp[i-2]+costi2)

再帰っぽい or for文

状態をまとめる

メモ化再帰

def rec(i):=i番目の足場に来るための最小コストを返す関数
  if i==0:#0番目は特に何もない
    return 0

  ret=min(rec(i-1)+cost,rec(i-2)+cost)

  return ret

再帰は時間がかかる
↓がいい

memo=[-1]*nを定義

def rec(i):=i番目の足場に来るための最小コストを返す関数
  if i==0:#0番目は特に何もない
    return 0

  if memo[i]!=-1:
    return memo[i]

  ret=min(rec(i-1)+cost,rec(i-2)+cost)

  return ret

一度調べたことを調べなくても良い

"""

n=int(input())

h=list(map(int,input().split()))

dp=[0]*n#i番目の足場に来るときの最小コスト

dp[0]=0
dp[1]=abs(h[1]-h[0])

for i in range(2,n):
    dp[i]=min(
        dp[i-1]+abs(h[i]-h[i-1]),
        dp[i-2]+abs(h[i]-h[i-2])
    )


print(dp[n-1])



