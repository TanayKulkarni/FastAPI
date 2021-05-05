from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_squared_error
import numpy as np 
# import pandas as pd

def ml(w,x,y,z): 

    df = load_iris()
    knn = KNeighborsClassifier(n_neighbors=4)
    p = {
        0: 'setosa',
        1: 'versicolor',
        2: 'virginica'
    }
    X_train,X_test,y_train,y_test = train_test_split(df['data'],df['target'],test_size = .2, random_state=42)

    knn.fit(X_train,y_train)

    y_pred = knn.predict(X_test)

    score = knn.score(X_test,y_test)

    mse = mean_squared_error(y_test,y_pred)


    # print(score)
    # print(mse)
    # print(y_pred)
    pred = knn.predict(np.array([[w,x,y,z]]))
    # print(p[pred[0]])
    return p[pred[0]]

# print(ml(2,3,1,3))