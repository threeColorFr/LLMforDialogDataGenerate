# 本地加载chatglm2模型
- 安装git lfs: [git-lfs](https://docs.github.com/zh/repositories/working-with-files/managing-large-files/installing-git-large-file-storage)
- 执行  GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/THUDM/chatglm2-6b
- 进入chatglm2-6b文件夹执行git lfs install 和 git lfs pull下载checkpoint
- 将加载代码中的 THUDM/chatglm2-6b 替换为你本地的 chatglm2-6b 文件夹的路径，即可从本地加载模型。

```
import os
os.environ['CUDA_VISIBLE_DEVICES']='0'

from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("chatglm2-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("chatglm2-6b", trust_remote_code=True, device='cuda')
model = model.eval()

response, history = model.chat(tokenizer, "你好", history=[])
print(response)
print(history)

response, history = model.chat(tokenizer, "晚上睡不着应该怎么办", history=history)
print(response)
```
