#Discretization
import numpy as np
import pandas as pd
from sklearn.preprocessing import KBinsDiscretizer
#create a sample DataFrame 
data={
'A':[1,2,4,5,6,8,7]
}
df=pd.DataFrame(data)
#Discretize the data into 3 bins
discretizer = KBinsDiscretizer(n_bins = 3,encode='ordinal',strategy='uniform')
df['A_binned']=discretizer.fit_transform(df[['A']])
print("Discretized DataFramr:n_bins=3 and strategy_uniform\n",df)

