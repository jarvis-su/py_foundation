'''
Author:     DuMin SONG
organization: 光环国际
Project:    regression_model
software:   PyCharm
'''
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot as plt
import joblib
cancer = load_breast_cancer()
X = cancer.get('data')
y = cancer.get('target')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15)
model = LogisticRegression(max_iter=3000)
model.fit(X_train,y_train)
#序列化，保存模型
# joblib.dump(model,'mylr.model')
date = np.arange(np.size(y_test)).reshape(-1)
print(date)
y_pre = model.predict(X_test)
score = model.score(X_test,y_test)
print(score)
print(model.coef_)
print(model.intercept_)
plt.scatter(date,y_test,color='g',marker='+')
plt.scatter(date,y_pre,color='r',marker='*')
plt.show()