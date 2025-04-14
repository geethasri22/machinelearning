import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
df = pd.read_csv("Example3.csv")
#specifying features and classifiers
features =['feature1','feature2']
x=df[features]
y=df['class']
rc=RandomForestClassifier()
model=rc.fit(x,y)
new_x=5
new_y=2
new_point=[(new_x,new_y)]
p=rc.predict(new_point)
print("testing pattern belongs to the class:",p,"based on random forest")
print("accuracy of the model:",metrics.accuracy_score([new_y],p))
tree=rc.estimators_[0]
plt.figure(figsize=(20,10))
plot_tree(tree,
       feature_names=df.columns.tolist(),
       filled=True,
rounded=True,
fontsize=10
)
plt.title("Decision Tree from random forest 0")
plt.show()
