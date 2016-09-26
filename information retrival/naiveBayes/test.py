import csv

from naiveBayes import MultinomialNB
import numpy as np


if __name__ == "__main__":
    X = np.array([
                      [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3],
                      [4,5,5,4,4,4,5,5,6,6,6,5,5,6,6]
                              ])
    X = X.T
    y = np.array([-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1])

    file = []
    cls = []
    cls_unique = {}
    with open('data.csv', 'r') as f:
        next(f)
        csv_file = csv.reader(f, delimiter=",")
        for line in csv_file:
            file.append(line[1:-1])
            cls.append(line[-1:])

        for line in file:
            for i in range(len(line)):
                line[i] = int(line[i])

    for u in np.unique(cls):
        cls_unique[u] = 0
    j = 0
    for i in cls_unique:
        cls_unique[i] = j
        j += 1
    for k in range(len(cls)):
        cls[k] = ''.join(cls_unique[cls[k]])
    A = np.array(file)
    A = A.T
    b = np.array(cls)
    print(b)







    nb = MultinomialNB(alpha=1.0,fit_prior=True)
    nb.fit(A,b)
    print( nb.alpha)
    print( nb.class_prior)
    print( nb.classes)
    print (nb.conditional_prob)
    print (nb.predict(np.array([2,4])))







    # nb1 = GaussianNB(alpha=0.0)
    # print nb1.fit(X,y).predict(X)