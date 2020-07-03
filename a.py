import pandas as pd

#1、读取数据集
wine = pd.read_csv('wine.csv')
winequality = pd.read_csv('winequality.csv',sep = ';')



#2、数据和标签拆分开
wine_data=wine.iloc[:,1:]
wine_target=wine['Class']
winequality_data=winequality.iloc[:,:-1]
winequality_target=winequality['quality']


#3、划分训练集和测试集
from sklearn.model_selection import train_test_split
wine_data_train, wine_data_test, \
wine_target_train, wine_target_test = \
train_test_split(wine_data, wine_target, \
    test_size=0.1, random_state=6)

winequality_data_train, winequality_data_test, \
winequality_target_train, winequality_target_test = \
train_test_split(winequality_data, winequality_target, \
    test_size=0.1, random_state=6)

#4、标准化数据集
from sklearn.preprocessing import StandardScaler #标准差标准化
stdScale = StandardScaler().fit(wine_data_train) #生成规则（建模）
wine_trainScaler = stdScale.transform(wine_data_train)#对训练集进行标准化
wine_testScaler = stdScale.transform(wine_data_test)#用训练集训练的模型对测试集标准化

stdScale = StandardScaler().fit(winequality_data_train)
winequality_trainScaler = stdScale.transform(winequality_data_train)
winequality_testScaler = stdScale.transform(winequality_data_test)

#5、PCA降维
from sklearn.decomposition import PCA
pca = PCA(n_components=5).fit(wine_trainScaler)
wine_trainPca = pca.transform(wine_trainScaler)
wine_testPca = pca.transform(wine_testScaler)

pca = PCA(n_components=5).fit(winequality_trainScaler)
winequality_trainPca = pca.transform(winequality_trainScaler)
winequality_testPca = pca.transform(winequality_testScaler)