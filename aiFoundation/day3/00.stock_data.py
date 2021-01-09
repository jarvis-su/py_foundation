'''
Author:     DuMin SONG
organization: 光环国际
Project:    regression_model
software:   PyCharm
'''
import tushare as ts
import pandas as pd
# 获取股票代码 600519是茅台
stock = ts.get_hist_data('600519')
# 保存为csv文件
stock.to_csv('600519.csv')
# 使用pandas读取csv文件
stock = pd.read_csv('600519.csv')
# 处理空值：1、扔掉空值； 2、补0 ；3、填充空值
# axis=0,按行删除；axis=1，按列删除；inplace=True，覆盖；inplace=False，不覆盖
stock.dropna(axis=0,inplace=True)
# date字段值改为日期类型
stock['date'] = pd.to_datetime(stock['date'])
# 排序ascending=True按升序排列
stock.sort_values(by=['date'],ascending=True,inplace=True)
# 设置索引
stock = stock.set_index('date')
# print(stock)
stock.to_csv('600519_V2.csv')