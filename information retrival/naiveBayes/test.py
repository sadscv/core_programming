import csv
import pprint

from naiveBayes import MultinomialNB
import numpy as np

file = []
cls = []
cls_unique = {}

def seperate():
    with open('data.csv', 'r') as f:
        next(f)
        csv_file = csv.reader(f, delimiter=",")
        for line in csv_file:
            file.append(line[1:-1])
            cls.append(line[-1:])
        for line in file:
            for i in range(len(line)):
                line[i] = int(''.join(line[i]))
        for i in range(len(cls)):
            cls[i] = ''.join(cls[i])
    for u in np.unique(cls):
        cls_unique[u] = 0
    j = 0
    for i in cls_unique:
        cls_unique[i] = j
        j += 1
    for k in range(len(cls)):
        temp = cls[k]
        cls[k] = cls_unique[temp]
    A = np.array(file)
    b = cls


    nb = MultinomialNB(alpha=1.0,fit_prior=True)
    nb.fit(A,b)
    print( nb.alpha)
    print( nb.class_prior)
    print( nb.classes)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(nb.conditional_prob)
    print (nb.conditional_prob)
    predict = []
    for i in range(len(A[0])):
        predict.append(i)
    print (nb.predict(np.array(predict)))

if __name__ == "__main__":
    X = np.array([
            [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],
            [4, 5, 5, 4, 4, 4, 5, 5, 6, 6, 6, 5, 5, 6, 6]
        ])
    X = X.T
    y = np.array([-1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1])
    seperate()

    # nb1 = GaussianNB(alpha=0.0)
    # print nb1.fit(X,y).predict(X)