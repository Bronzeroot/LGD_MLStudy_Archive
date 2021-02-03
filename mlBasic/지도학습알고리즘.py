from IPython.display import display
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn
import mglearn

#forge data생성 후 산점도
X,y = mglearn.datasets.make_forge()
mglearn.discrete_scatter(X[:,0],X[:,1],y)
plt.legend(["class 0", "class 1"], loc=4)
plt.xlabel("Character 1")
plt.ylabel("Character 2")
print("X.shapee:{}".format(X.shape))

#wave data생성 후 산점도
X,y = mglearn.datasets.make_wave(n_samples=40)
plt.plot(X,y,'o')
plt.ylim(-3,3)
plt.xlabel('Character')
plt.ylabel('Target')

#data shape 확인
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
print('cancer.keys(): \n{}'.format(cancer.keys()))
print("data shape : {}".format(cancer.data.shape))
print("Sample per class: \n{}".format(
    {n: v for n , v in zip(cancer.target_names, np.bincount(cancer.target))}))
print("CharacterName \n{}".format(cancer.feature_names))

#data shape 확인
from sklearn.datasets import load_boston
boston = load_boston()
print("data shape : \n{}".format(boston.data.shape))
X, y = mglearn.datasets.load_extended_boston()
print("X.shape: {}".format(X.shape))


#knn 예시
mglearn.plots.plot_knn_classification(n_neighbors=1)
mglearn.plots.plot_knn_classification(n_neighbors=3)
