import sys
print("python버전 : {}".format(sys.version))
import pandas as pd
print("pandas버전 : {}".format(pd.__version__))
import matplotlib
print("matplotlib 버전 : {}".format(matplotlib.__version__))
import numpy as np
print("numpy 버전 : {}".format(np.__version__))
import scipy as sp
print("Scipy 버전 :{}".format(sp.__version__))
import IPython
print("IPython버전 : {}".format(IPython.__version__))
import mglearn
import sklearn
from sklearn.datasets import load_iris
iris_dataset = load_iris()
print("iris_dataset의 키: \n{}".format(iris_dataset.keys()))
print(iris_dataset['DESCR']+"\n..")
print("타깃의 이름 : {}".format(iris_dataset['target_names']))
print("특성의이름 : {}".format(iris_dataset['feature_names']))
print("data의 타입:{}".format(type(iris_dataset['data'])))
print("data의크기:{}".format(iris_dataset['data'].shape))
print("data의 처음 다섯행 :\n{}".format(iris_dataset['data'][:5]))
print("target의 타입:{}".format(type(iris_dataset['target'])))
print("target의크기:{}".format(iris_dataset['target'].shape))
print("타깃:\n{}".format(iris_dataset['target']))

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(
    iris_dataset['data'],iris_dataset['target'],random_state=0)

print("X_train 크기:{}".format(X_train.shape))
print("y_train 크기:{}".format(y_train.shape))
print("X_test 크기{}".format(X_test.shape))
print("y_test 크기{}".format(y_test.shape))
