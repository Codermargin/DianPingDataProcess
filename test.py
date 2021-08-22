import numpy as np
import pandas as pd
from sklearn.datasets import load_iris


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


if __name__ == '__main__':
    dataset = load_iris()
    print(dataset['data'])
    data = pd.DataFrame(dataset['data'])
    dis = kmeans(data, 3)
    print(dis)
