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


#knn 예시
mglearn.plots.plot_knn_classification(n_neighbors=1)
mglearn.plots.plot_knn_classification(n_neighbors=3)


#K-최근접 이웃 

X, y = mglearn.datasets.load_extended_boston()
print("X.shape: {}".format(X.shape))

from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train,y_train)
print("Test set predict:{}".format(clf.predict(X_test)))
print("Test set Accuracy {:.2f}".format(clf.score(X_test, y_test)))

fig, axes = plt.subplots(1,3,figsize=(10,3))

for n_neighbors, ax in zip([1,3,9],axes):
    clf = KNeighborsClassifier(n_neighbors=n_neighbors).fit(X,y)
    mglearn.plots.plot_2d_separator(clf, X, fill=True, eps=0.5, ax=ax, alpha=.4)
    mglearn.discrete_scatter(X[:,0],X[:,1],y,ax=ax)
    ax.set_title("{} neighbor".format(n_neighbors))
    ax.set_xlabel("Character 0")
    ax.set_ylabel("Character 1")
axes[0].legend(loc=3)
