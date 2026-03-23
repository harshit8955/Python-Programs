import requests

# 🔑 Your OpenWeather API Key
API_KEY = "97e9356089d042467aeaccf96adfd7a4"

# 🌆 City name
city = "Sikar"

# 🌐 API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# 📡 Send request
response = requests.get(url)

# 📦 Convert to JSON
data = response.json()

# 🛑 Check if API call is successful
if response.status_code == 200:

    print("\n🌤 WEATHER DETAILS\n")

    # 🌡 Temperature
    print("Temperature:", data["main"]["temp"], "°C")
    print("Feels Like:", data["main"]["feels_like"], "°C")
    print("Min Temp:", data["main"]["temp_min"], "°C")
    print("Max Temp:", data["main"]["temp_max"], "°C")

    # 💧 Humidity & Pressure
    print("Humidity:", data["main"]["humidity"], "%")
    print("Pressure:", data["main"]["pressure"], "hPa")

    # 🌬 Wind
    print("Wind Speed:", data["wind"]["speed"], "m/s")

    # ☁ Weather Condition
    print("Weather:", data["weather"][0]["main"])
    print("Description:", data["weather"][0]["description"])

    # 🌍 Location
    print("City:", data["name"])
    print("Country:", data["sys"]["country"])

    # 🌅 Sunrise & Sunset
    print("Sunrise:", data["sys"]["sunrise"])
    print("Sunset:", data["sys"]["sunset"])

else:
    print("❌ Error:", data.get("message", "Something went wrong"))