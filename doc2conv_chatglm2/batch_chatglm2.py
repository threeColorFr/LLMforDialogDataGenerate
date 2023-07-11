import os
import sys
import re
os.environ['CUDA_VISIBLE_DEVICES']='0'

from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("../chatglm2-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("../chatglm2-6b", trust_remote_code=True, device='cuda')
model = model.eval()


prompt = '文档:\n{}'

his = [
    ('请根据文档生成一段两人对话，用A表示第一个人，B表示第二个人，对话以A开始，以B结束。\n\n文档:\n当网红、做直播，正成为不少年轻人期待的工作。微博近日发布一项“当代年轻人就业在关注什么”问卷数据：近万名受访应届毕业生中，61.6%的人就业时会考虑网红直播等新兴职业，只有38.4%选择完全不考虑。另有数据显示，2022年，直播、短视频行业直接或间接带动的就业机会超1亿个。越来越多年轻人“打开思路”，试图加入直播等新兴行业。但这行真的那么“好赚”吗？“网红”是不是个有前途的职业选择？大量应届毕业生加入直播行业据国是直通车，对于上述微博问卷数据，有12年就业辅导经验的职业发展经纪人佟志刚表示，该数据相对真实地反映了当前毕业生的求职预期变化。从他接触的求职者来看，2022年开始，越来越多应届毕业生希望能兼职做主播。',
    'A: 最近微博发布了一份关于年轻人就业关注点的问卷数据，显示有近万名受访的应届毕业生中，61.6%的人在就业时会考虑网红直播等新兴职业，而只有38.4%的人选择完全不考虑。这意味着越来越多的年轻人希望从事直播等新兴行业了。\nB: 是啊，我也听说了。我觉得这可能是因为直播、短视频行业在2022年带动的就业机会超过了1亿个，所以年轻人开始对这个行业产生了兴趣。\nA: 但是我一直在想，网红这个职业真的那么好赚吗？毕竟现在市场上已经有很多网红了，竞争应该很激烈吧。\nB: 对，竞争确实很激烈。我听说很多应届毕业生都想兼职做主播，但是不知道他们真的能在这个行业立足吗？')
    ]

def generate_conv(in_file, out_file, margin=500):
    '''
    功能： 读取输入文档，按照margin切分，分别生成对话数据，写入out_file文件。
    in_file: 输入原始文档
    out_file: 输出对话文件
    margin: 文档切分跨度
    '''
    print('Start:'+in_file)
    with open(in_file, 'r', encoding='utf-8') as fin,\
        open(out_file, 'w', encoding='utf-8') as fout:
        docs = fin.read().replace(' ', '')
        length = len(docs)
        index = 0
        while index<length:
            doc = docs[index:index+margin]
            
            # 生成对话
            input = prompt.format(doc)
            #print(input)
            response, history = model.chat(tokenizer, input, history=his)
            #print(response)
            response = re.sub('\n+','\n',response.strip()) # 规范输出
            fout.write(response)
            fout.write('\n\n\n') # 分割对话
            fout.flush()

            index+=margin
    print('Done:'+out_file)

""" 
#并行模型吃不消
import concurrent.futures
def call_for_all(in_dir, out_dir):
    files = os.listdir(in_dir)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for file in files:
            in_next = in_dir + '/' + file
            out_next = out_dir + '/' + file
            if os.path.isdir(in_next):
                os.makedirs(out_next, exist_ok=True)
                #call_for_all(in_next, out_next)
                futures.append(executor.submit(call_for_all, in_next, out_next))
            else:
                # 核心处理
                if os.path.getsize(in_next)<50: #跳过空的或者字较少的文档
                    continue

                pre, _ = os.path.splitext(out_next)
                out_next = pre + '.conv'
                #generate_conv(in_next, out_next)
                futures.append(executor.submit(generate_conv, in_next, out_next))
        # 等待所有任务完成
        print(futures)
        concurrent.futures.wait(futures) """

def call_for_all(in_dir, out_dir):
    files = os.listdir(in_dir)
    for file in files:
        in_next = in_dir + '/' + file
        out_next = out_dir + '/' + file
        if os.path.isdir(in_next):
            os.makedirs(out_next, exist_ok=True)
            call_for_all(in_next, out_next)
            
        else:
            # 核心处理
            if os.path.getsize(in_next)<50: #跳过空的或者字较少的文档
                continue

            pre, _ = os.path.splitext(out_next)
            out_next = pre + '.conv'
            try:
                generate_conv(in_next, out_next)
            except Exception as e:
                print(str(e))
                


#generate_conv('/data/weixiang/JiaotongGPT/Data_txt/泛研全球科研项目数据库/北京国内航线市场细分研究.txt', '1.txt')

# in_dir = sys.argv[1]
# out_dir = sys.argv[2]

# call_for_all('../Data_txt', '../Data_txt_conv')
call_for_all('../Data2_txt', '../Data2_txt_conv')
