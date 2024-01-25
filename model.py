import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

load_iris = load_iris()
dir(load_iris)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(load_iris.data,load_iris.target, test_size=0.2)

model.fit(X_train, y_train)


print(model.score(X_test, y_test))

model.predict(load_iris.data[100:150])

y_predicted = model.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_predicted)

# import seaborn as sn
# plt.figure(figsize = (10,7))
# sn.heatmap(cm, annot=True)
# plt.xlabel('Predicted')
# plt.ylabel('Truth')

import pickle
pickle.dump(model,open("model.pkl","wb"))