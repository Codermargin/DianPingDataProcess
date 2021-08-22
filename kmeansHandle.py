import json
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

import xlwt


def dist(x, y):
    xy = (sum((x - y) ** 2)) ** 0.5
    return (xy)


def kmeans(data, m):
    m = m
    name = ['center' + str(i) for i in range(m)]
    for j in range(len(name)):
        name[j] = data.iloc[j, :]

    dis = pd.DataFrame(index=range(len(data)), columns=range(len(name)))
    dis['class'] = 0

    while True:
        for i in range(len(data)):
            for k in range(len(name)):
                dis.iloc[i, k] = dist(data.iloc[i, :], name[k])

        for i in range(len(data)):
            dis.iloc[i, len(name)] = np.argmin(list(dis.iloc[i, 0:(len(name))]))

        index = ['index' + str(i) for i in range(m)]
        for q in range(m):
            index[q] = dis.iloc[:, len(name)] == q
        name2 = ['center_new' + str(i) for i in range(m)]
        for t in range(m):
            name2[t] = data.loc[index[t], :].mean()

        sum_s = []
        for w in range(m):
            sum_s.append(sum(name[w] == name2[w]))
        if sum(sum_s) == (m * (data.shape[1])):
            break

        for e in range(m):
            name[e] = name2[e]

    return dis

def useKMeans(inputArr):
    output_pred = KMeans(n_clusters=2, random_state=9).fit_predict(inputArr)
    plt.scatter(inputArr[:, 0], inputArr[:, 1], c=output_pred)
    plt.show()

def preparedata(vecResDic):
    inputArr = []
    for key in vecResDic:
        inputArr.append(vecResDic[key])
    print(inputArr)
    return inputArr

def readData(fileName):
    file = open(fileName,'r+')
    content = file.read()
    vecResDic = json.loads(content)
    print(vecResDic)
    file.close()
    return vecResDic

def saveResult(values,vecResDic):
    resultBook = xlwt.Workbook()
    KMeans_Sheet = resultBook.add_sheet(u'Kmeans数据结果', cell_overwrite_ok=True)
    wordsArr = []
    for key in vecResDic:
        wordsArr.append(key)
    for i in range(len(values)):
        KMeans_Sheet.write(i, 0, wordsArr[i])
        for j in range(len(values[0]) - 1):
            KMeans_Sheet.write(i, j+2, values[i][j])
        KMeans_Sheet.write(i,1,values[i][len(values[0]) - 1])
    resultBook.save('Kmeans结果.xlsx')

if __name__ == '__main__':
    fileName = '词语向量化后数据.txt'
    vecResDic = readData(fileName)
    # prepare data
    inputArr = preparedata(vecResDic)
    # use kmeans
    # useKMeans(inputArr)
    # multiple level kmeans
    data = pd.DataFrame(inputArr)
    kVal = 8
    res = kmeans(data,kVal)
    print(res)
    values = res.values;
    # res.plot(res['0'],res['1'],kind='scatter')
    # plt.show()
    # saveResult('聚类结果.txt',res)
    # 输出结果到excel
    saveResult(values,vecResDic)