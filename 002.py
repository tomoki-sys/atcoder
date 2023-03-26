"""


N=int(input())

li=[1,-1]

result=0

tmp=0

str=""

for i in range(1<<N):
  tmp=0
  str=""
  for j in range(N):
    if i&(1<<j):
      tmp+=1
      str+="("

    else:
      tmp-=1
      str+=")"

    if tmp<0:
      #print("a")
      break
    

  #print(tmp)
  result+=1
  print(str)


#print(result)

ビット全探索で全ての通りを作成してそれが正しい組であるかを検証するのもありかもしれない。


"""

from itertools import combinations

n=int(input())

if n%2==1:
    exit()

def to_parentehs(opens):
    chars=[")"]*n

    for open_pos in opens:
        chars[open_pos]='('

    return "".join(chars)

"""
6なら(1,4,5)などを作って、その部分のインデックスだけ（から）に帰る

そしてそれが、完全なカッコであるかを判定する

"""



for opens in combinations(list(range(n)),n//2):

    parentehs=to_parentehs(opens)
    cnt=0
    ok=True

    for c in parentehs:
        if c=="(":
            cnt+=1

        else:
            cnt-=1

        if cnt<0:
            ok=False

    if ok:
        print(parentehs)
    

    

