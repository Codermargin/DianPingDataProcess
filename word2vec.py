from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import xlrd
from text2vec import Word2Vec
import json


def readFromXls(fileName, sheetName):
    wordbook = xlrd.open_workbook_xls(fileName)
    wordSheet = wordbook.sheet_by_name(sheetName)
    sheetRows = wordSheet.nrows
    wordsArr = []
    for i in range(sheetRows):
        wordsArr.append(wordSheet.cell(i, 0).value);
    print(wordsArr)
    return wordsArr


def word2vecFunc(model, wordsArr):
    wordsArr_embeddings = model.encode(wordsArr)

    print(type(wordsArr_embeddings), wordsArr_embeddings.shape)

    # The result is a list of sentence embeddings as numpy arrays
    resVecDic = {}
    for word, embedding in zip(wordsArr, wordsArr_embeddings):
        resVecDic[word] = embedding.tolist()
        print("Word:", word)
        print("Embedding:", embedding)
        print(len(embedding))
        print("")
    return resVecDic


def saveDic(resVecDic):
    file = open('词语向量化后数据.txt', 'w+')
    file.write(json.dumps(resVecDic))
    file.close()
    print('保存完成txt数据...')


def sk2VecFunc(wordsArr):
    vectorizer = CountVectorizer(max_features=5)
    TF_Transformer = TfidfTransformer()
    TF_Res = TF_Transformer.fit_transform(vectorizer.fit_transform(wordsArr))
    vectorsRes = TF_Res.toarray()
    print(vectorsRes)
    return vectorsRes


if __name__ == '__main__':
    fileName = 'TF-IDF处理结果文件.xlsx'
    sheetName = 'TF-IDF数据报表（Topk=100)'
    wordsArr = readFromXls(fileName, sheetName)
    w2v_model = Word2Vec('w2v-light-tencent-chinese')
    resVecDic = word2vecFunc(w2v_model, wordsArr)
    saveDic(resVecDic)
    # sk2VecFunc(wordsArr)
