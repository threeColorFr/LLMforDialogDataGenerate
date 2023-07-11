# pdfOrdoc2txt-txt2dialog-llm
1. convert pdf or docx to txt; 从pdf或者docx中提取文本为txt文件
2. generate dialog data from txt documents using LLM like ChatGLM2 or ChatGPT； 利用ChatGLM2,ChatGPT等大模型根据文档生成对话数据集
## 整体步骤
1. 首先准备原始数据（pdf, docx, doc）; 存放在Data文件夹下(也可以自己重命名)，支持多级目录存放
2. 转换原始数据到txt文件中

- 首先`cd pdfOrdoc_mining`
- 执行`bash run.sh ../Data ../Data_txt`;其中两个参数分别表示`原始数据目录`和`生成的txt存放的目录`
- 环境：`pdfminer`, `docx2txt`包

3. 根据txt文件中的document，利用LLM ChatGLM2生成对话数据

- 首先  `cd doc2conv_chatglm2`
- 执行 `bash run.sh`; 注意修改batch_chatglm2.py文件中的参数：`call_for_all('../Data_txt', '../Data_txt_conv')`; Data_txt_conv文件夹是生成的对话数据存放目录
- 环境见 [ChatGLM2](https://github.com/THUDM/ChatGLM2-6B); chatglm2-6b是本地加载时存放模型的文件夹，详情见[about](https://github.com/threeColorFr/pdfOrdoc2txt-txt2dialog-llm/blob/main/chatglm2-6b/readme.md)

