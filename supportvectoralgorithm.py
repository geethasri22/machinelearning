import numpy as np
from sklearn import svm
from sklearn.svm import SVC
from sklearn.inspection import DecisionBoundaryDisplay
import matplotlib.pyplot as plt
x=np.array(
[
 [2,1],
[1,3],
[6,3],
]
)
y=np.array([-1,-1,1])
sv=SVC(kernel='linear')
model=sv.fit(x,y)
new_x=2
new_y=0
new_point=[(new_x,new_y)]
p=sv.predict(new_point)
print("testing pattern belongs to the class:",p,"using svm")
print("support  vectors are:")
def plot_training_data_with_decision_boundary(kernel):
    fig, ax=plt.subplots(figsize=(10,10))
    x_min,x_max,y_min,y_max=0,10,0,10
    ax.set(xlim=(x_min,x_max),ylim(y_min,y_max))
    common_param={"estimators":sv,"x":x,"ax":ax}
    DecisionBoundaryDisplay.from_estimators(
        **commom_params,
        plot_method="contour",
        levels=[-1,0,1]
        colors=["b","r","g"]
        linestyles=["--","-","--"]
        )
sc=ax.scatter(x[:,0],x[:,1],c=y,s=450)
ax.scatter(x[:,0],x[:,1],c=y,s=450)
ax.legend(*sc.legend_elements(),loc="upper right",title="classes")
plot_training_data_with_decision_boundary("linear")
plt.show()
