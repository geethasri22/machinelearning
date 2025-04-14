#applying preprocessing techniques of a given data
#1)attributes 

#attribute selection
import pandas as pd
from sklearn.datasets import load_iris,load_diabetes,load_wine
from sklearn.feature_selection import SelectKBest,f_classif

#load iris dataset
d=load_iris()
X=pd.DataFrame(d.data , columns=d.feature_names)
y=pd.Series(d.target)

#select the top 2 features
selector = SelectKBest(score_func=f_classif,k=2)
X_selected = selector.fit_transform(X,y)
print("selected features of iris database : \n",X.columns[selector.get_support()])


#load daibetes set
d=load_diabetes()
X=pd.DataFrame(d.data , columns=d.feature_names)
y=pd.Series(d.target)

#select the top2 features
selector = SelectKBest(score_func=f_classif,k=2)
X_selected = selector.fit_transform(X,y)
print("selected features of iris database : \n",X.columns[selector.get_support()])


#load wine database
d=load_wine()
X=pd.DataFrame(d.data , columns=d.feature_names)
y=pd.Series(d.target)

#select the top2 features
selector = SelectKBest(score_func=f_classif,k=2)
X_selected = selector.fit_transform(X,y)
print("selected features of iris database : \n",X.columns[selector.get_support()])

