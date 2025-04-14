#preprocessing technique as handling missing values
import pandas as pd
import numpy as np
data = {
'A':[1,2, np.nan, 4],
'B':[np.nan, 2,3,4],
'C':[1,2,3,4]
}
df=pd.DataFrame(data)
df_dropped = df.dropna()
df_filled = df.fillna(df.mean())
print("DataFrame after dropping missing values:\n",df_dropped)
print("DataFrame after filling missing values:\n",df_filled)
