import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
df = pd.read_csv("Example5.csv")
#specifying features and classifiers
features =['feature1','feature2']
x=df[features]
y=df['target']
dtree=DecisionTreeRegressor()
model=dtree.fit(x.values,y.values)
p=dtree.predict([[0.7,0.5]])
print("predicted values using DTR:",p)
plt.figure(figsize=(10,10))
plot_tree(
       dtree,
       filled=True,
rounded=True,
fontsize=10
)
plt.title("Decision Tree Regressor")
plt.show()
