#! /usr/bin/env python
import csv
import os
import sys
import re

import numpy as np
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer

class classifier():

    features = []
    list = []

    def _tokenize(self, text):
        terms = re.findall(r'\w+', text)
        # re.findall() return a list
        #  e.g. ['this', 'is', 'a', 'test', '0']
        terms = [term for term in terms if not term.isdigit()]
        return terms

    # pattern = r'''(?x)    # set flag to allow verbose regexps
    #      ([A-Z]\.)+        # abbreviations, e.g. U.S.A.
    #    | \w+(-\w+)*        # words with optional internal hyphens
    #    | \$?\d+(\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
    #    | \.\.\.            # ellipsis
    #    | [][.,;"'?():-_`]  # these are separate tokens
    #    '''


    #return a dict which contained
    #the top 10 most-frequent words
    def _frequency(self, text):
        sent = self._tokenize(text)
        ans = {}
        for i in sent:
            if i not in stopwords.words():
                #stemming
                las = LancasterStemmer()
                temp = las.stem(i)
                if temp not in ans:
                    ans[temp] = 1
                else:
                    ans[temp] += 1
        sorted(ans, key=ans.get, reverse=True)
        ans2 = {}
        for i in list(ans)[0:10]:
            ans2[i] = ans[i]
        return ans2



    def _write(self):
        #when opening files which are not supposed to be text,
        # even in Unix, you should use wb or rb.
        # Use plain w or r only for text files.
        with open("data.csv", 'w') as f:
            csv_file = csv.writer(f, delimiter=",")
            row = list(self.features)
            row.insert(0, " ")
            row.append(" ")
            csv_file.writerow(row)
            for i in self.list:
                row = [i[0]]
                count = 0
                for j in self.features:
                    if j in i[1].keys():
                        row.append(i[1][j])
                    else:
                        row.append(0)
                    count += 1
                row.append(i[2])
                csv_file.writerow(row)



    def train(self):
        #__file__ 是用来获得模块所在的路径的，这可能得到的是一个相对路径，
        dataset_path = os.path.dirname(os.path.realpath(__file__))
        for dirname in os.listdir(dataset_path):
            label = dirname
            classpath = os.path.join(dataset_path, dirname)
            for dirpath, dirnames, filenames in os.walk(classpath):
                print('#' * 80)
                print('Entering directory: %s' % dirpath)
                filenum = 0
                fileamounts = len(filenames)
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    with open(filepath, 'r') as f:
                        filenum += 1
                        print('finished:%.1f=========>training %s ' % (100 *(filenum/fileamounts), filename))
                        freq = self._frequency(f.read())
                        for i in freq.keys():
                            if i not in self.features:
                                self.features.append(i)
                        self.list.append((filepath, freq, label))
        self._write()


    def test(self):
        with open(sys.argv[2]) as f:
            total_words = len(self.features)
            num_words = {}
            for i in self.list:
                temp = 0
                for j in i[1]:
                    temp += i[1][j]
                if i[2] not in num_words:
                    num_words[i[2]] = temp
                else:
                    num_words[i[2]] += temp

            words = self._frequency(f.read())

        prob = {}
        for i in num_words.keys():
            prob[i] = 1.0
        for i in words.keys():
            for k in num_words.keys():
                count = 0
                for j in self.list:
                    if j[2] == k and i in j[1].keys():
                        count += j[1][i]
                post = (count + 1.0)/(total_words + num_words[k])
                # ** 求幂
                prob[k] *= (post ** words[i])

        print(prob)


        # calculate class_prior
        # classes = []
        # class_prob = {}
        # for i in self.list:
        #     classes.append(i[2])
        # classes_num = len(classes)
        # for t in np.unique(classes):
        #     class_prob[t] = 0
        # for c in classes:
        #     class_prob[c] += 1
        # print('#' *80 )
        # print(class_prob)





        max = -1.0
        classfied = ""
        for i in prob:
            if prob[i] * num_words[i] > max:
                max = prob[i] * num_words[i]
                classfied = i
        print(classfied)

    def showmenu(self):
        pr = '''
        (T)rain
        t(E)st
        (V)iew
        (Q)uit

        Please Enter choice:
        '''
        while True:
            while True:
                try:
                    choice = input(pr).strip()[0].lower()
                except (EOFError, KeyboardInterrupt, IndexError):
                    choice = 'q'

                print('You picked:[%s]' % choice)
                if choice not in 'tevq':
                    print('invalid option, try again')
                else:
                    break
            if choice == 't':
                self.train()
            if choice == 'e':
                self.test()
            if choice == 'v':
                print(self.features)
            if choice == 'q':
                break


if __name__ == '__main__':
    k = classifier()
    k.showmenu()
