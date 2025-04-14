import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
df = pd.read_csv("Example3.csv")
#specifying features and classifiers
features =['feature1','feature2']
x=df[features]
y=df['class']
dtree=DecisionTreeClassifier()
model=dtree.fit(x,y)
tree.plot_tree(model,feature_names=features)
dt_text=tree.export_text(dtree)
print(dt_text)
