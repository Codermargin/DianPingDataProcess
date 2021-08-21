import sys
import jieba
import xlrd
import jieba.analyse

# 1.JieBa分词测试
# [数据配置] 从Excel表格中读取评论数据
wordbook = xlrd.open_workbook_xls(r'大众点评图书馆数据xls.xls')
SZ_sheet = wordbook.sheet_by_name('深圳图书馆')
# print(SZ_sheet.row_values(1))
sheet_rows = SZ_sheet.nrows
content = ''
for i in range(1,sheet_rows):
    content = content + SZ_sheet.cell(i,0).value + ';' +SZ_sheet.cell(i,1).value
print(content)
# content = '特别喜欢氛围感觉安静上自习课学习的氛围因为安静干净桌面上带有充电插座很多人会带电脑学习沉浸学习阅读很愉快得享受'

# 1.1 自定义分词词典导入
words = ['会带','很愉快']
for word in words:
    jieba.add_word(word)
# Jieba 分词测试
# HMM=False
# cutResult = '/'.join(jieba.cut(content,HMM))
# print(cutResult)

# 2.自定义停用词词典导入
# 停用词
stopWordsFilePath = '停用词表Gy.txt' #停用词表路径
jieba.analyse.set_stop_words(stopWordsFilePath)


# 3.使用TF-IDF划分出所有的权重关键词，并返回权重系数
# topK 返回几个 TF/IDF 权重最大的关键词
topK = 100


withWeight = True # 是否返回权重值
result = jieba.analyse.extract_tags(content,topK,withWeight)
print(result)

