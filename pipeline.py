#create pipeline

import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score

df=pd.read_csv("D:\Python_Satish_Gupta\D_danial\Machine learning\ml_pipeline\dataset1\data.csv")

df['churn']=df['churn'].replace(('yes','no'),(1,0))

X=df.drop(['churn'],axis=1)
y=df['churn']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)

categorical_columns=list(X_train.select_dtypes(include=['object']).columns.values.tolist())

numerical_columns=list(X_train.select_dtypes(exclude=['object']).columns.values.tolist())

numeric_transformer=SimpleImputer(strategy='constant')


s=SimpleImputer(strategy='most_frequent')
o=OneHotEncoder(handle_unknown='ignore')
a=[('simple_imputer',s),('onehot_encoder',o)]

categorical_transformer=Pipeline(steps=a)

b=[
	('numeric',numeric_transformer,numerical_columns),
	('categorical',categorical_transformer,categorical_columns),
]

preprocessor=ColumnTransformer(transformers=b)

model=XGBClassifier(random_state=0,scale_pos_weight=6)

bundled_pipeline=Pipeline(steps=[
	('preprocessor',preprocessor),
	('model',model)])

bundled_pipeline.fit(X_train,y_train)

y_pred=bundled_pipeline.predict(X_test)
roc_auc=roc_auc_score(y_test,y_pred)
accuracy=accuracy_score(y_test,y_pred)

print('ROC/AUC:',roc_auc)
print('Accuracy:',accuracy)
