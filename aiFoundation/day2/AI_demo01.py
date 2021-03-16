import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import  LinearRegression

China = []
with open(file='../../data/owid-covid-data.csv', mode='r', encoding='utf-8') as f:
    data = f.readlines()
    for line in data:
        field = [item for item in line.split(',')]
        if field[2] == 'China':
            China.append(field[4])
China = np.array(China, dtype=np.float).astype(int)
np.savez('covid-China', China=China)
logging.debug(China)

X = np.arange(np.size(China)).reshape(-1, 1)

model =  LinearRegression()
model.fit(X, China)

y = model.predict(X)
# logging.debug(model.coef_)
# logging.debug(mode)


plt.scatter(X,China)
plt.plot(X, y, color='r')
# plt.plot

plt.show()