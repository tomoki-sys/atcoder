"""
動的計画法
ナップザック問題
https://www.youtube.com/watch?v=Y0UEyW64CzM&list=PLwlP26Z1O_DesFumSto6rfa9T2jmk9iD4&index=2


"""
#%%
#動的計画法
N=5
length=10
li=[4,7,8,5,1]

dp=[[False for _ in range(length+1)] for _ in range(N+1)]

dp[0][0]=True

#True＝作れる　False=作れない

for i in range(N):#行
    for j in range(length):#列
        if dp[i][j]:
            dp[i+1][j]=True
            #上の値をそのまま反映させる
            if j+li[i]<=length:
                #新しく追加された棒が表の範囲内なら
                dp[i+1][j+li[i]]=True

if dp[-1][-1]:
    print("OK")

            



#6*11の表ができる

#%%
#ナップザック問題
N=5
length=10
li=[4,7,8,5,1]

money=500
price=[150,200,250,200,50]

money=money//50#全部50刻みの値段になっているから
price=list(map(lambda x: x//50,price))
print(price,money)

dp=[[-1 for _ in range(money+1)] for _ in range(N+1)]

for j in range(length+1):
    dp[0][j]=0

for i in range(N):
    for j in range(money+1):
        #price[i] 新たに追加された棒の値段
        #財布の中身の上限
        if price[i] <=j:
            #上のモノをそのままスライド
            dp[i+1][j]=max(dp[i][j],dp[i][j-price[i]]+li[i])
            #買うか買わないか

        else:
            dp[i+1][j]=dp[i][j]
                          
            
print(dp[-1][-1])



# %%
dp

# %%
