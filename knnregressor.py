import pandas as pd
from sklearn import linear_model
from sklearn.neighbors import KNeighborsRegressor
#Trainig patterns
df = pd.read_csv("example2.csv")
X=df([['length','weight']])
y=df['cost']
r=linear_model.LinearRegression()
r.fit(X.values,y.values)
y_p=r.predict([[0.3,0.4]])
print("predicted value using linear regression is:",y_p)
knn_r=KNeighborsRegressor(n_neighbors=5)
knn_r.fit(X.values,y.values)
y_p_r=knn_r.predict([[0.3,0.4]])
print("predicted value using KNN is:",y_p_r)
