import os ;os.system('cls')
import pandas as pd
import matplotlib.pyplot as p
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
"""
EDA part-2
IT contain -detecting & remove outliers 
           -Encoding categorized value
           -Feature Scaling
           -data splitting
"""
df=pd.read_excel("cleaned_india_aqi_data.xlsx")
print(df)
# Removing & detected outliers
# z-score for df["PM2.5"]
mean =df["PM2.5"].mean()
std= df["PM2.5"].std()
lower_limit=mean-3*std
upper_limit=mean+3*std
print(f"The lower limit is {lower_limit}")
print(f"The upper limit is {upper_limit}")
# finding out the outliers
outliers1 =df.loc[(df["PM2.5"]>upper_limit) | (df["PM2.5"]<lower_limit)]
print(f"Checking for outliers in PM2.5: {outliers1}")
# for df["PM10"]
mean1 =df["PM10"].mean()
std1= df["PM10"].std()
lower_limit1=mean1-3*std1
upper_limit1=mean1+3*std1
print(f"The lower limit is {lower_limit1}")
print(f"The upper limit is {upper_limit1}");
# finding out the outliers
outliers2 =df.loc[(df["PM2.5"]>upper_limit) | (df["PM2.5"]<lower_limit)]
print(f"Checking outliers for PM10: {outliers2}")
# for df["SO2"]
mean1 =df["SO2"].mean()
std1= df["SO2"].std()
lower_limit2=mean1-3*std1
upper_limit2=mean1+3*std1
print(f"The lower limit is {lower_limit2}")
print(f"The upper limit is {upper_limit2}")
# finding out the outliers
outliers3 =df.loc[(df["SO2"]>upper_limit) | (df["SO2"]<lower_limit)]
print(f"checking outliers for SO2 :{outliers3}")
# hence there are no outliers
# encoding categorizes value
# on hot encoding
df_encoded=df.copy()
df_encoded.drop(columns=["Dominant_Pollutant"], inplace=True)
print(f" The dataFrame we are working on{df_encoded}")
df_encoded =pd.get_dummies(df_encoded)
# Convert only city dummy columns to int, keep others as float
dummy_cols = [col for col in df_encoded.columns if 'City_' in col]
df_encoded[dummy_cols] = df_encoded[dummy_cols].astype(int)
print("\n Encoded data : ")
# for select dummies column only
dummy_cols = [col for col in df_encoded.columns if 'City_' in col] 
# converting bit into a string 
df_encoded['bit_string'] = df_encoded[dummy_cols].apply(lambda row: ''.join(row.astype(str)), axis=1)
print(f"converting into one bit encoded data : {df_encoded}")
df_encoded.to_excel("data_for_model.xlsx")# write a last
# training and test sets(data splitting)
drop_list=["Time_2021-11-15 06:00:00","AQI"]
X=df_encoded.drop(drop_list,axis=1)
y=df_encoded["AQI"]
X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.2,random_state=11)# here test will have 20% of data
print(f"The part left for testing:{X_test}")
print(f"The part on which we train the module: {X_train}")
# feature scaling(not needed here)
scaler =StandardScaler()
scaler.fit(X_train)# here we try to learn from X_train, and taking it's data 
X_train_scaler =scaler.transform(X_train)# applying the formula
X_test_scaler= scaler.transform(X_test)# it will return array
# converting into dataframe
X_test_scaler=pd.DataFrame(X_test_scaler,columns=X_test.columns)
print(f"The standardization on test data : {X_test_scaler}")
X_train_scaler=pd.DataFrame(X_train_scaler,columns=X_train.columns)
print(f"The standardization on train data:{X_train_scaler}")
# showing standardization
r=np.round(X_train.describe(),decimals=1)
print(f"It is used to show before standardization :{r}")
r1=np.round(X_train_scaler.describe(),decimals=1)
print(f"It is used to show after standardization :{r1}")