# Created by Joe Habre
import requests

API_KEY = "8698ca8bbea014ad06763b1b79775a23"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data["cod"] != 200:
            print(f"❌ Error: {data['message']}")
            return

        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        print(f"\n🌤️ Weather in {city_name}, {country}")
        print(f"🌡️ Temperature: {temp}°C")
        print(f"🌬️ Wind Speed: {wind} m/s")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌈 Condition: {desc.capitalize()}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("🌦️ Real-Time Weather App\n")
    while True:
        city = input("Enter city name (or 'q' to quit): ")
        if city.lower() == 'q':
            print("👋 Exiting Weather App.")
            break
        get_weather(city)

