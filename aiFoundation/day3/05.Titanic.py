'''
Author:     DuMin SONG
organization: 光环国际
Project:    regression_model
software:   PyCharm
'''
# 导入Python三剑客
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv('Titanic.csv')

# 观察数据
data.info()

# 可视化显示
plt.subplot(221)
data.Survived.value_counts().plot(kind='bar')
plt.title('获救人数（1为获救）',fontname='SimHei')
plt.ylabel('人数',fontname='SimHei')
plt.grid(True,axis='y')
# plt.show()

plt.subplot(222)
data.Pclass.value_counts().plot(kind='bar')
plt.title('乘客仓位分布',fontname='SimHei')
plt.ylabel('人数',fontname='SimHei')
plt.grid(True,axis='y')
# plt.show()

plt.subplot(223)
data.Sex.value_counts().plot(kind='bar')
plt.title('乘客性别',fontname='SimHei')
plt.ylabel('人数',fontname='SimHei')
plt.grid(True,axis='y')
# plt.show()

plt.subplot(224)
data.Embarked.value_counts().plot(kind='bar')
plt.title('乘客上船地点分布',fontname='SimHei')
plt.ylabel('人数',fontname='SimHei')
plt.grid(True,axis='y')
plt.show()

# data.Age[data.Pclass=='1'].plot(kind='kde')
# data.Age[data.Pclass=='2'].plot(kind='kde')
# data.Age[data.Pclass=='3'].plot(kind='kde')
# plt.legend(('1st','2nd','3rd'))
# plt.grid(True)
# plt.title('乘客年龄和船舱等级分布',fontname='SimHei')
# plt.ylabel('人数密度',fontname='SimHei')
# plt.show()


s=data.Sex[data.Survived== 1].value_counts()
ds=data.Sex[data.Survived== 0].value_counts()
a_s=pd.DataFrame({u'saved':s,u'dontsaved':ds})
a_s.plot.bar(stacked=True)
plt.xlabel('性别',fontname='SimHei')
plt.ylabel('人数',fontname='SimHei')
plt.title('性别和获救人数的分布',fontname='SimHei')
plt.grid(True,axis='y')
# plt.show()


s=data.Pclass[data.Survived== 1].value_counts()
ds=data.Pclass[data.Survived== 0].value_counts()
p_s=pd.DataFrame({u'saved':s,u'dontsaved':ds})
p_s.plot.bar(stacked=True)
plt.xlabel('客舱等级',fontname='SimHei')
plt.ylabel('人数',fontname='SimHei')
plt.title('客舱等级和获救人数的分布',fontname='SimHei')
plt.grid(True,axis='y')
# plt.show()


s=data.Embarked[data.Survived== 1].value_counts()
ds=data.Embarked[data.Survived== 0].value_counts()
e_s=pd.DataFrame({u'saved':s,u'dontsaved':ds})
e_s.plot.bar(stacked=True)
plt.xlabel('上船地点',fontname='SimHei')
plt.ylabel('人数',fontname='SimHei')
plt.title('上船地点和获救人数的分布',fontname='SimHei')
plt.grid(True,axis='y')
# plt.show()


has_cabin=data.Survived[pd.notnull(data.Cabin)].value_counts()
donthas_cabin=data.Survived[pd.isnull(data.Cabin)].value_counts()
c_s=pd.DataFrame({u'has':has_cabin,u'donthave':donthas_cabin})
c_s.plot.bar(stacked=True)
plt.xlabel('有无cabin',fontname='SimHei')
plt.ylabel('人数',fontname='SimHei')
plt.title('有无cabin和获救人数的分布',fontname='SimHei')
plt.grid(True,axis='y')
plt.show()

def process_data(df):
    # 处理pclass
    p_index = df['Pclass'].unique().tolist()
    df['Pclass'] = df['Pclass'].apply(lambda x: p_index.index(x))

    # 处理embarked
    e_index = df['Embarked'].unique().tolist()
    df['Embarked'] = df['Embarked'].apply(lambda x: e_index.index(x))

    # 处理sex
    df.loc[df['Sex'] == 'male', 'Sex'] = 1
    df.loc[df['Sex'] == 'female', 'Sex'] = 0
    return df

# 丢弃训练集中无用列
df=process_data(data).drop(['Ticket','Name','Fare'],axis=1)
df.loc[df.Age.isnull(), 'Age'] = 0
df.loc[df['Age']<10,'Age']=0
df.loc[(df['Age']>=10)&(df['Age']<20),'Age']=1
df.loc[(df['Age']>=20)&(df['Age']<30),'Age']=2
df.loc[(df['Age']>=30)&(df['Age']<40),'Age']=3
df.loc[(df['Age']>=40)&(df['Age']<50),'Age']=4
df.loc[(df['Age']>=50)&(df['Age']<60),'Age']=5
df.loc[df['Age']>=60,'Age']=6

# 处理cabin
df['has_cabin']=df['Cabin'].apply(lambda x: 0 if pd.isnull(x) else 1)

# 合并sibsp和parch 到family
df['Family']=df['SibSp']+df['Parch']
# print(df)

# 使用决策树模型
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

sur_df = df[['Pclass', 'Survived', 'Sex', 'Age', 'Embarked', 'has_cabin', 'Family']]
X = sur_df.drop('Survived', axis=1).values
y = sur_df['Survived'].values

# 划分验证集（0.2）和训练集（0.8）
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
rfc_sur = RandomForestClassifier(n_estimators=100)
rfc_sur.fit(X_train, y_train)


print("train score:", rfc_sur.score(X_train, y_train))
print("test score:", rfc_sur.score(X_test, y_test))