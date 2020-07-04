#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

wine = pd.read_csv('./data/wine.csv')
winequality = pd.read_csv('./data/winequality.csv',sep = ';')

wine_data=wine.iloc[:,1:]
wine_target=wine['Class']
winequality_data=winequality.iloc[:,:-1]
winequality_target=winequality['quality']

from sklearn.model_selection import train_test_split
wine_data_train, wine_data_test, wine_target_train, wine_target_test = train_test_split(wine_data, wine_target,     test_size=0.1, random_state=6)

winequality_data_train, winequality_data_test, winequality_target_train, winequality_target_test = train_test_split(winequality_data, winequality_target,     test_size=0.1, random_state=6)

from sklearn.preprocessing import StandardScaler #标准差标准化
stdScale = StandardScaler().fit(wine_data_train) #生成规则（建模）
wine_trainScaler = stdScale.transform(wine_data_train)#对训练集进行标准化
wine_testScaler = stdScale.transform(wine_data_test)#用训练集训练的模型对测试集标准化

stdScale = StandardScaler().fit(winequality_data_train)
winequality_trainScaler = stdScale.transform(winequality_data_train)
winequality_testScaler = stdScale.transform(winequality_data_test)

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters = 3,random_state=1).fit(wine_trainScaler)
print('构建的KMeans模型为：\n',kmeans)


from sklearn.metrics import fowlkes_mallows_score 
score=fowlkes_mallows_score(wine_target_train,kmeans.labels_)
print("wine数据集的FMI:%f"%(score))

for i in range(2,11):
    kmeans = KMeans(n_clusters = i,random_state=123).fit(wine_trainScaler)
    score = fowlkes_mallows_score(wine_target_train,kmeans.labels_)
    print('wine数据聚%d类FMI评价分值为：%f' %(i,score))

from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
silhouettteScore = []
for i in range(2,11):
    kmeans = KMeans(n_clusters = i,random_state=1).fit(wine)
    score = silhouette_score(wine,kmeans.labels_)
    silhouettteScore.append(score)
plt.figure(figsize=(10,6))
plt.plot(range(2,11),silhouettteScore,linewidth=1.5, linestyle="-")
plt.savefig('image1.png')
plt.show()

from sklearn.metrics import calinski_harabaz_score
for i in range(2,11):
    kmeans = KMeans(n_clusters = i,random_state=1).fit(wine)
    score = calinski_harabaz_score(wine,kmeans.labels_)
    print('wine数据聚%d类calinski_harabaz指数为：%f'%(i,score))



