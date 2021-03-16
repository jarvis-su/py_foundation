'''
Author:     DuMin SONG
organization: 光环国际
Project:    regression_model
software:   PyCharm
'''
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
stock = pd.read_csv('600519_V3.csv')
data = stock.values
y = data[:, -1:]
X = data[:,:-1]
# print(X)
# print(y)
day = np.arange(np.size(y)).reshape(-1, 1)
# plt.plot(day,y)
# plt.show()
y_train = y[:-120, :]
X_train = X[:-120, :]
y_test = y[-120:, :]
X_test = X[-120:, :]
day_train = day[:-120, :]
day_test = day[-120:, :]
# print(X_train,X_test,y_train,y_test)
# print(day_train,day_test)
pi_line = Pipeline([('poly', PolynomialFeatures(degree=1)),
                    ('st', StandardScaler()),
                    ('lr', LinearRegression())])
pi_line.fit(X_train,y_train)
y_pre = pi_line.predict(X_test)
# plt.plot(day_train,y_train,color='b')
plt.plot(day_test,y_test,color='g')
plt.plot(day_test,y_pre,color='r')
plt.show()

score = pi_line.score(X_test,y_test)

print(score)

# pre_to = pd.read_csv('600519_V3.csv')
# value = pre_to.values
# X_to = value[:,1:]
# # print(X_to)
# pre_mo = pi_line.predict(X_to)
# print(pre_mo)