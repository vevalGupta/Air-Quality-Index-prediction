import os;os.system('cls')
import pandas as pd
import matplotlib.pyplot as p
"""
Step-3 EDA(exploratory data Analysis)
"""
df =pd.read_excel("cleaned_india_aqi_data.xlsx")
print(df)
# 1) descriptive Statistics
# # a)Measure of central tendency
print(f"Maximum AQI: {df["AQI"].max()}")# issue
print(f" Minimum AQi: {df["AQI"].min()}")#issue
# # mean
print(f" Mean of all PM2.5 : {df["PM2.5"].mean()}")
print(f"  Mean of all PM10 : {df["PM10"].mean()}")
print(f"  Mean of all NO2 : {df["NO2"].mean()}")
print(f"  Mean of all SO2 : {df["SO2"].mean()}")
print(f"  Mean of all CO : {df["CO"].mean()}")
print(f"  Mean of all O3 : {df["O3"].mean()}")
print(f"  Mean of all Temperature (°C) : {df["Temperature (°C)"].mean()}")
print(f"  Mean of all Humidity (%) : {df["Humidity (%)"].mean()}")
print(f" Mean of all Pressure (hPa) : {df["Pressure (hPa)"].mean()}")
print(f" Mean of all Wind Speed (m/s) : {df["Wind Speed (m/s)"].mean()}")
# # mode
print(f" Mode of all PM2.5 : {df["PM2.5"].mode()}")
print(f"  Mode of all PM10 : {df["PM10"].mode()}")
print(f"  Mode of all NO2 : {df["NO2"].mode()}")
print(f"  Mode of all SO2 : {df["SO2"].mode()}")
print(f"  Mode of all CO : {df["CO"].mode()}")
print(f"  Mode of all O3 : {df["O3"].mode()}")
print(f"  Mode of all Temperature (°C) : {df["Temperature (°C)"].mode()}")
print(f"  Mode of all Humidity (%) : {df["Humidity (%)"].mode()}")
print(f" Mode of all Pressure (hPa) : {df["Pressure (hPa)"].mode()}")
print(f" Mode of all Wind Speed (m/s) : {df["Wind Speed (m/s)"].mode()}")
# # median
print(f" Median of all PM2.5 : {df["PM2.5"].median()}")
print(f"  Median of all PM10 : {df["PM10"].median()}")
print(f"  Median of all NO2 : {df["NO2"].median()}")
print(f"  Median of all SO2 : {df["SO2"].median()}")
print(f"  Median of all CO : {df["CO"].median()}")
print(f"  Median of all O3 : {df["O3"].median()}")
print(f"  Median of all Temperature (°C) : {df["Temperature (°C)"].median()}")
print(f"  Median of all Humidity (%) : {df["Humidity (%)"].median()}")
print(f" Median of all Pressure (hPa) : {df["Pressure (hPa)"].median()}")
print(f" Median of all Wind Speed (m/s) : {df["Wind Speed (m/s)"].median()}")
# # Standard deviation
print(f"standard deviation of AQi :{df["AQI"].std()}")
print(f"standard deviation of PM10 :{df["PM10"].std()}")
print(f"standard deviation of NO2  :{df["NO2"].std()}")
print(f"standard deviation of SO2 :{df["SO2"].std()}")
print(f"standard deviation of CO :{df["CO"].std()}")
print(f"standard deviation of O3 :{df["O3"].std()}")
print(f"standard deviation of Temperature (°C) :{df["Temperature (°C)"].std()}")
print(f"standard deviation of Humidity (%) :{df["Humidity (%)"].std()}")
print(f"standard deviation of Pressure (hPa) :{df["Pressure (hPa)"].std()}")
print(f"standard deviation of Wind Speed (m/s) :{df["Wind Speed (m/s)"].std()}")
# Data Visualization
cities = [
    "Major Dhyan Chand National Stadium, Delhi, Delhi, India",
    "Kurla, Mumbai, India",
    "Ballygunge, Kolkata, India",
    "Royapuram, Chennai, Chennai, India",
    "Hombegowda Nagar, Bengaluru, India",
    "Somajiguda, Hyderabad, India",
    "Shivajinagar, Pune, Pune, India",
    "Maninagar, Ahmedabad, India",
    "Police Commissionerate, Jaipur, India",
    "Central School, Lucknow, India",
    "Sector 22, Chandigarh, India",
    "T T Nagar, Bhopal, India",
    "IGSC Planetarium Complex, Patna, India",
    "FTI Kidwai Nagar, Kanpur, India"
]
new_city=["Delhi","Mumbai","Kolkata","Chennai","Bengaluru","Hyderabad","Pune","Ahmedabad","Jaipur","Lucknow","Chandigarh","Bhopal","Patna","Kanpur"]
colors = [
    "#FF6F61",  # Coral Red
    "#6B5B95",  # Purple
    "#88B04B",  # Olive Green
    "#F7CAC9",  # Light Pink
    "#92A8D1",  # Soft Blue
    "#955251",  # Brown
    "#B565A7",  # Violet
    "#009B77",  # Teal Green
    "#DD4124",  # Orange-Red
    "#45B8AC",  # Aqua Blue
    "#EFC050",  # Golden Yellow
    "#5B5EA6",  # Indigo
    "#9B2335",  # Dark Red
    "#BC243C"   # Crimson
]
p.bar(df["City"],df["AQI"],color="red")
p.xlabel("Cities")
p.ylabel("AQI")
p.title("Compare air quality levels among different cities.")
p.xticks(cities,new_city)
p.savefig("Bar_Graph.png",dpi=200,bbox_inches='tight')
p.show()
# it is easy to see which cities have the highest or lowest air pollution levels.
# 2. scatter plot
p.scatter(df["Wind Speed (m/s)"],df["AQI"],colorizer="black")
p.xlabel("Wind speed(m/s)")
p.ylabel("AQI")
p.title("Understand how wind affects air quality")
p.xlim(0,15)
p.ylim(0,400)
p.savefig("Scatter_plot.png",dpi=200,bbox_inches='tight')
p.show()
# if higher wind speed lowers AQI, you’ll notice a downward trend — meaning wind helps disperse pollutants.
# 3.Scatter plot-2
p.scatter(df["Temperature (°C)"],df["AQI"],colorizer="black")
p.xlabel("Temperature (°C)")
p.ylabel("AQI")
p.title("Study the relationship between temperature and pollution")
p.xlim(0,40)
p.ylim(0,400)
p.savefig("Scatter_plot-2.png",dpi=200,bbox_inches='tight')
p.show()
# Helps reveal if high temperatures correlate with poor or better air quality.
# 4. pie chart
p.pie(df["PM2.5"],labels=new_city,colors=colors,autopct="%1.1f%%")
p.title("Show which pollutant is dominant most often across cities.")
p.savefig("Pie_chart.png",dpi=200,bbox_inches='tight')
p.show()
# You’ll see which pollutant (like PM2.5 or NO₂) most frequently causes poor air quality in India.
# 5. line Graph
p.plot(df["Humidity (%)"],df["AQI"],linestyle="--")
p.title("Observe whether humidity influences air quality.")
p.xlabel("Humidity (%)")
p.ylabel("AQI")
p.xlim(0,130)
p.ylim(0,350)
p.tight_layout()   # Adjust spacing
p.savefig("line_Graph.png",dpi=200,bbox_inches='tight')
p.show()
# Helps identify if humid air traps pollutants or disperses them.
# 6.heatmap
D={
    'AQI': [290, 85, 40, 96, 48, 132, 232, 101, 175, 153, 106, 98, 52, 105],
    'PM2.5': [290, 85, 40, 96, 48, 132, 232, 101, 175, 153, 106, 98, 52, 105],
    'PM10': [224, 50, 13, 67, 35, 64, 138, 55, 133, 60, 55, 57, 52.50, 48],
    'NO2' : [28.40, 1.50, 22.50, 14.20, 4, 4.50, 198, 10.30, 31.40, 10.80, 22.40, 7.20, 6.60, 9.10],
    'SO2' :[13, 14.90, 2.60, 2.40, 4.60, 5.90, 6.30, 6.70, 2.30, 4.50, 2.80, 2.40, 11.80, 13.10],
    'CO' :[8.30, 1, 1.50, 1.85, 2.20, 4.10, 51, 6.70, 10.60, 7.70, 6.10, 5.20, 12.50, 6.40],
    'O3':[3.10, 11.40, 5.90, 7.20, 4.90, 4.30, 61, 18, 3.40, 10.40, 4.80, 10.30, 19.90, 8.70]
}
semi_df =pd.DataFrame(D)
heat=semi_df.corr()
print(f"correlation between AQI Parameters: \n{heat}")
p.figure(figsize=(7,7))
p.imshow(heat,cmap="YlOrRd")
p.colorbar()
p.title("correlation matrix")
p.xticks(range(7),heat.index)
p.yticks(range(7),heat.index)
# code to write value in between the figure
for i in range(7):
    for j in range(7):# here we use lop to place corr() in correct place
        p.text(i,j,"{:.2f}".format(heat.values[i, j]))#used to put text of head variable

p.savefig("Heat_map.png",dpi=200,bbox_inches='tight')
p.show()
# Darker colors show stronger relationships — e.g., AQI is usually highly correlated with PM2.5.
