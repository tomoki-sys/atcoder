#%%
import torch

#%%
x=torch.rand(5,3)
print(x)
# %%
class Net(nn.Module):
    def __init__(self) -> None:
        super().__init__()