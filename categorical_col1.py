import pandas as pd 
from sklearn.model_selection import train_test_split 
 
df = pd.read_csv("D:\Python_Satish_Gupta\D_danial\Machine learning\ml_pipeline\dataset1\data.csv") 
df['churn'] = df['churn'].replace(('yes', 'no'), (1, 0)) 
 
X = df.drop(['churn'], axis=1) 
y = df['churn'] 
 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 
  0.3, random_state = 0) 
 
categorical_columns = list(X_train.select_dtypes(include =  
   ['object']).columns.values.tolist()) 

numerical_columns=list(X_train.select_dtypes(exclude=['object']).columns.values.tolist())

 
print(categorical_columns) 

print(numerical_columns)