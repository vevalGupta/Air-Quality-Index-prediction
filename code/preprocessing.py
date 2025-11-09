import os;os.system('cls')
# import API_multiple 
"""
STAGE-2 PREPROCESSING
"""
# first 3 line can be deleted
import pandas as pd
df=pd.read_excel("india_aqi_data.xlsx")
# I. Basic task
# this method is used to print the top 5 rows of the data
print(f"The first 5 rows :\n{df.head()}")
# this method is used to print the last 5 rows of the data
print(f"The last 5 row  are\n:{df.tail()}")
# to find shape of dataFrame
print(f"The shape of dataFrame : {df.shape}")
# to find basic information about the data
print("basic information about dataFrame:")
print(df.info())
# summarize the data 
print("summarization of dataset:")
print(df.describe())
# II. Handling missing value
# 1).isnull()->to find the missing value within the dataframe
print("Number of nan(not a number) present in column:\n")
print(df.isnull().sum())# return a boolean value
# 2).interpolation()-> used to fill Nan data according to it type used.
df["PM10"]=pd.to_numeric(df["PM10"])# used because some time numerical data is written in string in dataframe
df["SO2"]=pd.to_numeric(df["SO2"])
df["CO"]=pd.to_numeric(df["CO"])
df["Pressure (hPa)"]=pd.to_numeric(df["Pressure (hPa)"])
df=df.interpolate(method="linear")
print(f" Data with no missing value: {df}")
# used to check whether the missing data is fully filled or not
print(df.isnull().sum())
# III. sorting
print("The City with most Aqi:\n")
sort_city=df.sort_values(by="AQI",ascending=False)
print(sort_city[['City','AQI']])# it is used to only show city and AQI
# IV. Duplication
# it is used to count duplicate row in data frame
print(f"Total number of duplicated row:{df.duplicated().sum()} ")
# altering the data
def label_aqi(aqi):
    if aqi <= 50:
        return 'Good'
    elif aqi <= 100:
        return 'Satisfactory'
    elif aqi <= 200:
        return 'Moderate'
    elif aqi <= 300:
        return 'Poor'
    elif aqi <= 400:
        return 'Very Poor'
    else:
        return 'Severe'
    

# Apply function to create new column
df['AQI_Scale'] = df['AQI'].apply(label_aqi)
print(f"The dataset after addition : {df}")
# LAST PART save
df.to_excel("cleaned_india_aqi_data.xlsx",index=False)# index will remove sequence 