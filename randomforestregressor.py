import pandas
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
df = pandas.read_csv("Example3.csv")
#specifying features and classifiers
features =['feature1','feature2']
x=df[features]
y=df['target']
r=RandomForestRegressor()
model=r.fit(x,y)
p=r.predict([[0.3,0.4]])
print("predicted value using RF is:",p)
tree=r.estimators_[0]
plt.figure(figsize=(20,10))
plot_tree(tree,
       feature_names=df.columns.tolist(),
       filled=True,
rounded=True,
fontsize=10
)
plt.title("Decision Tree from random forest 0")
plt.show()
