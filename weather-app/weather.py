# Created by Joe Habre
import os
import requests
from datetime import datetime

API_KEY = os.environ.get("OPENWEATHER_API_KEY", "")
if not API_KEY:
    raise SystemExit("❌ Set the OPENWEATHER_API_KEY environment variable before running.")
BASE_URL = "https://api.openweathermap.org/data/2.5"

CONDITION_ICONS = {
    "clear": "☀️",
    "cloud": "☁️",
    "rain": "🌧️",
    "drizzle": "🌦️",
    "thunderstorm": "⛈️",
    "snow": "❄️",
    "mist": "🌫️",
    "fog": "🌫️",
    "haze": "🌫️",
    "smoke": "🌫️",
    "dust": "🌫️",
    "sand": "🌫️",
    "tornado": "🌪️",
}

recent_cities = []


def condition_icon(description):
    desc = description.lower()
    for keyword, icon in CONDITION_ICONS.items():
        if keyword in desc:
            return icon
    return "🌡️"


def wind_direction(deg):
    dirs = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    return dirs[round(deg / 45) % 8]


def fetch(endpoint, params):
    params["appid"] = API_KEY
    response = requests.get(f"{BASE_URL}/{endpoint}", params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    if data.get("cod") not in (200, "200"):
        raise ValueError(data.get("message", "Unknown error"))
    return data


def get_current(city, units):
    data = fetch("weather", {"q": city, "units": units})
    unit_sym = "°C" if units == "metric" else "°F"
    speed_sym = "m/s" if units == "metric" else "mph"

    name = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    feels = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    wind_deg = data["wind"].get("deg", 0)
    desc = data["weather"][0]["description"]
    icon = condition_icon(desc)
    sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M")
    sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M")

    print(f"\n{icon}  {name}, {country}")
    print(f"  🌡️  Temp      : {temp}{unit_sym}  (feels like {feels}{unit_sym})")
    print(f"  💧 Humidity  : {humidity}%")
    print(f"  🌬️  Wind      : {wind_speed} {speed_sym} {wind_direction(wind_deg)}")
    print(f"  🌈 Condition : {desc.capitalize()}")
    print(f"  🌅 Sunrise   : {sunrise}    🌇 Sunset: {sunset}")


def get_forecast(city, units):
    data = fetch("forecast", {"q": city, "units": units, "cnt": 24})
    unit_sym = "°C" if units == "metric" else "°F"

    print(f"\n📅 3-Day Forecast for {city.title()}")
    seen_dates = []
    for item in data["list"]:
        date_str = item["dt_txt"].split(" ")[0]
        if date_str in seen_dates:
            continue
        if len(seen_dates) >= 3:
            break
        seen_dates.append(date_str)
        date = datetime.strptime(date_str, "%Y-%m-%d").strftime("%a %d %b")
        temp = item["main"]["temp"]
        desc = item["weather"][0]["description"]
        icon = condition_icon(desc)
        print(f"  {date}  {icon}  {temp}{unit_sym}  {desc.capitalize()}")


def toggle_units(current):
    new = "imperial" if current == "metric" else "metric"
    print(f"✅ Switched to {'Imperial (°F)' if new == 'imperial' else 'Metric (°C)'}")
    return new


def show_history():
    if not recent_cities:
        print("  (no recent searches)")
    else:
        for i, city in enumerate(recent_cities, 1):
            print(f"  {i}. {city}")


def main():
    units = "metric"
    print("🌦️  Real-Time Weather App")
    print("  Commands: a city name  |  'f <city>' for forecast  |  'u' toggle units  |  'h' history  |  'q' quit")

    while True:
        sym = "°C" if units == "metric" else "°F"
        raw = input(f"\n[{sym}] Enter city (or command): ").strip()

        if not raw:
            continue

        if raw.lower() == "q":
            print("👋 Goodbye!")
            break

        elif raw.lower() == "u":
            units = toggle_units(units)

        elif raw.lower() == "h":
            show_history()

        elif raw.lower().startswith("f "):
            city = raw[2:].strip()
            if not city:
                print("❌ Provide a city name after 'f'.")
                continue
            try:
                get_forecast(city, units)
                if city.title() not in recent_cities:
                    recent_cities.insert(0, city.title())
                    if len(recent_cities) > 5:
                        recent_cities.pop()
            except ValueError as e:
                print(f"❌ {e}")
            except requests.RequestException as e:
                print(f"❌ Network error: {e}")

        else:
            try:
                get_current(raw, units)
                if raw.title() not in recent_cities:
                    recent_cities.insert(0, raw.title())
                    if len(recent_cities) > 5:
                        recent_cities.pop()
            except ValueError as e:
                print(f"❌ {e}")
            except requests.RequestException as e:
                print(f"❌ Network error: {e}")


if __name__ == "__main__":
    main()
