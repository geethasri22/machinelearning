import pandas
from sklearn.naive_bayes import MultinomialNB
df = pandas.read_csv("example7.csv")
#specifying features and classifiers
features =['feature1','feature2','feature3']
x=df[features]
y=df['class']
n=MultinomialNB()
model=n.fit(x,y)
new_x=1
new_y=1
new_z=0
new_point=[(new_x,new_y,new_z)]
p=n.predict(new_point)
print("testing pattern belongs to the class:",p,"using naive bayes classifier")

