# coding:utf-8
import os
import sys
import re
from pdfminer.converter import LTChar, TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox
from io import StringIO
from io import open

#读取pdf文件文本内容
def read(path):
    parser = PDFParser(path)
    doc = PDFDocument(parser, '')
    parser.set_document(doc)
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建PDf 资源管理器 来管理共享资源
        rsrcmgr = PDFResourceManager()
        # 创建一个PDF聚合器，包含资源管理器与参数分析器
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        # 创建一个PDF解释器对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        # 循环遍历列表，每次处理一个page的内容
        page0 = ''
        for i, page in enumerate(PDFPage.create_pages(doc)):
            interpreter.process_page(page)
            print("START PAGE %d\n" % i)
            if page is not None:
                interpreter.process_page(page)
            print("END PAGE %d\n" % i)
            # 接受该页面的LTPage对象
            layout = device.get_result()
            print(layout)
            # 这里layout是一个LTPage对象，里面存放着这个 page 解析出的各种对象
            # 包括 LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等
            line0 = ''
            for x in layout:
                if isinstance(x, LTTextBox):
                    line0 = line0 + x.get_text().strip()
            page0 = page0 + line0
        return page0 #返回pdf文件中所有提取到的文本内容


# 处理单个pdf
file = sys.argv[1]
outputfile = sys.argv[2]


pdffile = open(file, "rb")
content = read(pdffile)

pre, _ = os.path.splitext(outputfile)
outputfile = pre + '.txt' # 输出文件后缀修改

with open(outputfile, 'w+', encoding='utf8') as f:
    f.write(content)

print("DONE:" + outputfile)

# python main_pdf.py ../Data/泛研全球科研项目数据库/北京国内航线市场细分研究.pdf temppdf2txt.pdf