# pdfOrdoc2txt-txt2dialog-llm
Generate dialog data from documents using LLM like ChatGLM2 or ChatGPT；

利用ChatGLM2,ChatGPT等大模型根据文档生成对话数据集

生成效果如下：
```
A: 你好，我最近看到了一篇关于北京国内航线市场细分的文章，感觉挺有意思的。
B: 是啊，我也注意到了。这个研究旨在为航空公司进入北京航线市场、合理选择运营航线提供参考依据。
A: 文章提出了构建航线分类指标体系的方法，并利用因子分析对13个分类指标进行简化降维，提取了5个公因子。
B: 对，没错。然后，计算5个公因子的因子得分值，并以其为分类变量的系统聚类分析，以伪F统计量作为确定最佳分类数的指标。
A: 聚类结果表明，97条航线可以显著地分为7类细分市场。
B: 没错，这表明北京国内航线市场具有一定的特点和差异性，需要针对不同市场细分制定相应的运营策略。
A: 文章还对这些细分市场的特点进行了分析，为航空公司提供了有价值的参考。
B: 对，这个研究对于航空公司制定运营策略、合理分配资源非常有帮助。


A: 我也听说现在航空公司很难获取有效的起降时刻，这对我们的运营航线提出了很大的挑战。
B: 是的，而且现在市场竞争也很激烈，我们需要利用有限的时刻资源，选择收益较好的航线，提高我们的竞争力和盈利能力。
A: 那么有没有什么方法可以对北京国内航线市场进行细分，指导航空公司正确把握航线市场呢？
B: 有一些研究成果可以作为参考，但是目前还没有专门针对民航航线市场细分的研究。
A: 我听说有一篇文献[5]主要依据客流量对航线进行分类，将北京国内航线市场分为快线市场、大客流市场、中客流市场和低客流市场。
B: 是的，这篇文献主要研究了客流量对航线的影响，但是没有涉及细分市场的问题。
A: 那有没有其他的方法可以对市场进行细分呢？
B: 有一些研究使用聚类分析对航线市场上的旅客进行分类，但这些研究主要针对的是旅客类型和消费行为特征，没有涉及市场细分的概念。
A: 我听说有一篇文献[6]根据航线的市场集中度、客流量和收益水平，利用两阶段聚类法将美国国内O&D市场分成了7类，并对每个类别进行了投资组合分析。
B: 是的，这篇文献使用了一些方法对市场进行细分，但是这些方法主要是基于市场的因素，而不是旅客的特征。

```
## 整体步骤
1. 首先准备原始数据（pdf, docx, doc）; 存放在Data文件夹下(也可以自己重命名)，支持多级目录存放；doc需要先转换成docx，批量转见[about](https://github.com/threeColorFr/pdfOrdoc2txt-txt2dialog-llm/blob/main/Data/readme.md)
2. 转换原始数据到txt文件中

- 首先`cd pdfOrdoc_mining`
- 执行`bash run.sh ../Data ../Data_txt`;其中两个参数分别表示`原始数据目录`和`生成的txt存放的目录`
- 环境：`pdfminer`, `docx2txt`包

3. 根据txt文件中的document，利用LLM ChatGLM2生成对话数据

- 首先  `cd doc2conv_chatglm2`
- 执行 `bash run.sh`; 注意修改batch_chatglm2.py文件中的参数：`call_for_all('../Data_txt', '../Data_txt_conv')`; Data_txt_conv文件夹是生成的对话数据存放目录
- 环境见 [ChatGLM2](https://github.com/THUDM/ChatGLM2-6B); chatglm2-6b是本地加载时存放模型的文件夹，详情见[about](https://github.com/threeColorFr/pdfOrdoc2txt-txt2dialog-llm/blob/main/chatglm2-6b/readme.md)

ps: 也可以利用chatgpt生成，见`doc2conv_chatgpt`文件夹
