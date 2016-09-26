import numpy as np

class MultinomialNB(object):
    def __init__(self, alpha=1.0,fit_prior=True,class_prior=None):
        self.alpha = alpha
        self.fit_prior = fit_prior
        self.class_prior = class_prior
        self.classes = None
        self.conditional_prob = None

    def _caculate_feature_prob(self, feature):
        values = np.unique(feature)
        total_num = float(len(feature))
        value_prob = {}
        for v in values:
            value_prob[v] = ((np.sum(np.equal(feature, v)) + self.alpha) /
                              (total_num + len(values) * self.alpha))
        return value_prob
    def fit(self, X, y):
        self.classes = np.unique(y)
        #计算类别的先验概率
        if self.class_prior == None:
            class_num = len(self.classes)
            if not self.fit_prior:
                self.class_prior = [1.0 / class_num for _ in range(class_num)]
            else:
                self.class_prior = []
                sample_num = float(len(y))
                for c in self.classes:
                    c_num = np.sum(np.equal(y, c))
                    self.class_prior.append(
                        (c_num + self.alpha) / (sample_num + class_num*self.alpha)
                    )

        self.conditional_prob = {}
        for c in self.classes:
            self.conditional_prob[c] = {}
            for i in range(len(X[0])):

                # X = np.array([
                #     [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],
                #     [4, 5, 5, 4, 4, 4, 5, 5, 6, 6, 6, 5, 5, 6, 6],
                #     [4, 5, 5, 4, 4, 4, 5, 5, 6, 6, 6, 5, 5, 6, 6]
                # ])
                # ​
                # print(X[:,2])
                # [1 5 5]
                feature = X[np.equal(y,c)][:, i]
                self.conditional_prob[c][i] = self._caculate_feature_prob(feature)
        return self

    def _get_xj_prob(self, value_prob, target_value):
        return value_prob[target_value]

    def _predicct_single_sample(self, x):
        label = -1
        max_posterior_prob = 0

        for c_index in range(len(self.classes)):
            current_class_prior = self.class_prior[c_index]
            current_conditional_prob = 1.0
            feature_prob = self.conditional_prob[self.classes[c_index]]
            j = 0
            for feature_i in feature_prob.keys():
                current_conditional_prob *= self._get_xj_prob(feature_prob[feature_i], x[j])
                j += 1

            if current_class_prior * current_conditional_prob > max_posterior_prob:
                max_posterior_prob = current_conditional_prob * current_conditional_prob
                label = self.classes[c_index]

        return label

    def predict(self, X):
        if X.ndim == 1:
            return self._predicct_single_sample(X)
        else:
            labels = []
            for i in range(X.shape[0]):
                label = self._predicct_single_sample(X[i])
                label.append(label)
            return labels