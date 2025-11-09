import os;os.system('cls')
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
"""
We are using : Random forest(Advance machine learning)
Random forest is a supervised learning algorithm because it requires labeled data to train on for both classification and regression tasks.
"""
df_encoded=pd.read_excel("data_for_model.xlsx")
# removing unnecessary columns
df_encoded = df_encoded.drop(columns=["Unnamed: 0", "bit_string"], errors='ignore')# series of number (column)
df_encoded = df_encoded.drop([col for col in df_encoded.columns if "Time_" in col], axis=1)
# creating training data
X = df_encoded.drop(columns=["AQI"])
y=df_encoded["AQI"]
X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.3,random_state=11)# here test will have 20% of data
print(f"The part left for testing:{X_test}")
print(f"The part on which we train the module: {X_train}")
# training the random forest
model=RandomForestRegressor(n_estimators=150,max_depth=6,bootstrap=True,min_samples_split=8,
    random_state=42,min_samples_leaf=6,max_features="sqrt")
model.fit(X_train,y_train)
# time to find prediction
predicted=model.predict(X_test)# here it's predicting of test part which has 3 data rows 
pr =model.predict(X_train)
print(f"The predicted value by model(on training dataset): {pr}")
print(f"the predicted value by model(On testing dataset): {predicted}")# return array
# find accuracy of the model
accuracy = model.score(X_test,y_test)
acc=model.score(X_train,y_train)
print(f"The accuracy of training: {acc}")
print(f"The accuracy of testing :{accuracy}")
# check if it overfitting or underfitting
if acc > accuracy: print("It is overfitting ")
else : print("It is underfitting")
