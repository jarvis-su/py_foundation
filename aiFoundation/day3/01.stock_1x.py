'''
Author:     DuMin SONG
organization: 光环国际
Project:    regression_model
software:   PyCharm
'''
# ctrl + alt + l 规范代码
# ctrl + d 复制行
# ctrl + / 注释取消注释
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

stock = pd.read_csv('600519_V3.csv')
data = stock.values
# print(data)
y = data[:, -1:]
# print(y)
X = np.arange(np.size(y)).reshape(-1, 1)
# print(X)
# print(y)
# plt.plot(X,y)
# plt.show()
y_train = y[:-120, :]
X_train = X[:-120, :]
y_test = y[-120:, :]
X_test = X[-120:, :]
# print(X_train,X_test,y_train,y_test)
# model = LinearRegression()
# model.fit(X_train,y_train)
# y_pre = model.predict(X_test)
# plt.plot(X_train,y_train,color='b')
# plt.plot(X_test,y_test,color='g')
# plt.plot(X_test,y_pre,color='r')
# plt.show()
pi_line = Pipeline([('poly', PolynomialFeatures(degree=2)),
                    ('st', StandardScaler()),
                    ('lr', LinearRegression())])

pi_line.fit(X_train,y_train)
y_pre_po = pi_line.predict(X_test)
plt.plot(X_train,y_train,color='b')
plt.plot(X_test,y_test,color='g')
plt.plot(X_test,y_pre_po,color='r')
plt.show()
