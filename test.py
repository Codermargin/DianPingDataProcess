import sys
import jieba
import xlrd
import xlwt
import jieba.analyse


def readExcelData(fileName,sheetName):
    # 1.JieBa分词测试
    # [数据配置] 从Excel表格中读取评论数据
    wordbook = xlrd.open_workbook_xls(fileName)
    SZ_sheet = wordbook.sheet_by_name(sheetName)
    # print(SZ_sheet.row_values(1))
    sheet_rows = SZ_sheet.nrows
    content = ''
    for i in range(1, sheet_rows):
        content = content + SZ_sheet.cell(i, 0).value + ';' + SZ_sheet.cell(i, 1).value
    print(content)
    return content


# content = '特别喜欢氛围感觉安静上自习课学习的氛围因为安静干净桌面上带有充电插座很多人会带电脑学习沉浸学习阅读很愉快得享受'
def loadDic():
    # 1.1 自定义分词词典导入
    words = ['会带', '很愉快']
    for word in words:
        jieba.add_word(word)
    # Jieba 分词测试
    # HMM=False
    # cutResult = '/'.join(jieba.cut(content,HMM))
    # print(cutResult)

def loadStopWordDic():
    # 2.自定义停用词词典导入
    # 停用词
    stopWordsFilePath = '停用词表Gy.txt'  # 停用词表路径
    jieba.analyse.set_stop_words(stopWordsFilePath)


def TFIDFAnalysis(content,topK):
    # 3.使用TF-IDF划分出所有的权重关键词，并返回权重系数
    # topK 返回几个 TF/IDF 权重最大的关键词
    withWeight = True  # 是否返回权重值
    result = jieba.analyse.extract_tags(content, topK, withWeight)
    print(result)
    return result


def ouputData(result,topK):
    resultBook = xlwt.Workbook()
    TF_Sheet = resultBook.add_sheet(u'TF-IDF数据报表（Topk=100)', cell_overwrite_ok=True)
    # 写入数据
    for i in range(topK):
        TF_Sheet.write(i, 0, result[i][0])
        TF_Sheet.write(i, 1, result[i][1])
    resultBook.save('TF-IDF处理结果文件.xlsx')

if __name__ == '__main__':
    fileName = '大众点评图书馆数据xls.xls'
    sheetName = '深圳图书馆'
    content = readExcelData(fileName,sheetName)
    loadDic()
    loadStopWordDic()
    result = TFIDFAnalysis(content,topK=100)
    ouputData(result,topK=100)