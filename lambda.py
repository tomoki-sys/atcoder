"""
pythonのラムダ式を知る
無名関数
"""
#%%
def calc(base,height):
    return base*height//2

a=(lambda base,height:base*height//2)
#(lambda 引数:返り値)()
# %%
calc(5,2)
# %%
a(10,4)

# %%
#lambda式の強みは、map等と同時に用いる場合

students=["Imanishi","Imanyu","saito","suzuki","tanaka"]

#内包表記で書く場合
print([i.upper() for i in students])

# %%
#lambda式を使う場合
list(map(lambda i:i.upper(),students))

# %%
