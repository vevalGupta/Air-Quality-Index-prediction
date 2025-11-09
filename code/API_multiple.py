import requests
import pandas as pd
import time

# From WAQI Api key
API_KEY = "892eef92b26117c8553dd93aefabb6f83d8740c7"
# Api key provide access to use data 
cities = [
    "delhi", "mumbai", "kolkata", "chennai", "bengaluru",
    "hyderabad", "pune", "ahmedabad", "jaipur", "lucknow",
    "chandigarh", "bhopal", "patna", "kanpur", "visakhapatnam"
]# this is used for accessing each cities by changing city_name in url

# to collect city data
all_data = []
for city in cities:
    url = f"https://api.waqi.info/feed/{city}/?token={API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        if data.get("status") == "ok":
            # Extract Main and Inner Data
            info = data.get("data", {})#->main(contains AQI, city info, pollutant info, etc.)
            iaqi = info.get("iaqi", {})#->inner(stores values of PM2.5, NO2, etc)

            city_data = {
                "City": info.get("city", {}).get("name", city),
                "AQI": info.get("aqi"),
                "Dominant_Pollutant": info.get("dominentpol"),
                "PM2.5": iaqi.get("pm25", {}).get("v"),
                "PM10": iaqi.get("pm10", {}).get("v"),
                "NO2": iaqi.get("no2", {}).get("v"),
                "SO2": iaqi.get("so2", {}).get("v"),
                "CO": iaqi.get("co", {}).get("v"),
                "O3": iaqi.get("o3", {}).get("v"),
                "Temperature (°C)": iaqi.get("t", {}).get("v"),
                "Humidity (%)": iaqi.get("h", {}).get("v"),
                "Pressure (hPa)": iaqi.get("p", {}).get("v"),
                "Wind Speed (m/s)": iaqi.get("w", {}).get("v"),
                "Time": info.get("time", {}).get("s")
            }

            all_data.append(city_data)
            print(f" Collected Aqi for {city}")
        else:
            print(f"Skipped {city}: {data.get('data')}")

        # Small delay to avoid API rate limit
        time.sleep(100)

    except Exception as e:
        print(f" Error for {city}: {e}")

# Convert to DataFrame
df = pd.DataFrame(all_data)
# Save to CSV file
df.to_excel("india_aqi_data.xlsx", index=False)
print("\n Successfully collection")
print(df.head())
