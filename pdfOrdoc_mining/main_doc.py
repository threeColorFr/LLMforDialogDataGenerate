import sys
import os
import docx2txt
# python main_doc.py ../Data2/百度教育/常识/“交通”简介、含义、起源、历史及发展.docx tempdoc2txt1.docx

in_file = sys.argv[1] # ../Data2/百度教育/常识/“交通”简介、含义、起源、历史及发展.docx
out_file = sys.argv[2] # tempdoc2txt1.docx
pre, _ = os.path.splitext(out_file)
out_file = pre + '.txt' # 输出文件后缀修改

# method 1
text = docx2txt.process(in_file)
fw = open(out_file, 'w')
fw.write(text)
fw.close()

""" 
# method 2
import docx
doc_file = docx.Document(in_file)

fw = open(out_file, 'w')
for para in doc_file.paragraphs:
    fw.write(para.text)
    fw.flush()
fw.close() """