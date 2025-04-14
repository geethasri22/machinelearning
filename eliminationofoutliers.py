#Elimination of Outliers
import pandas as pd
#Create sample Data Frame
data= {
'A':[-5,-25,50,6,7,8,9,10,20]
}
print("Initial Data:\n",data)
df=pd.DataFrame(data)
#Caluculate Q1(25th percentile) and Q3(75th percentile)
Q1=df['A'].quantile(0.25)
Q3=df['A'].quantile(0.75)
print("quantile 1:",Q1)
print("quantile 3:",Q3)
IQR = Q3-Q1
print("InterQuartileRange:",IQR)
#define bounds for outliers
lower_bound = Q1-1.5*IQR
upper_bound = Q3+1.5*IQR
#Elimination outliers
df_no_outliers = df[(df['A'] >= lower_bound) & (df['A'] <= upper_bound)]
print("DataFrame after removing outliers:\n",df_no_outliers)


                    
