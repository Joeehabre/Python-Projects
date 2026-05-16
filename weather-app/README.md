# 🌦️ Weather App

Real-time weather and 3-day forecast in your terminal, powered by the OpenWeatherMap API.

---

## ✨ Features

- 🌡️ Temperature + feels-like
- 🌬️ Wind speed and direction (N / NE / E …)
- 💧 Humidity
- 🌅 Sunrise & sunset times
- 📅 3-day forecast (`f <city>`)
- 🔄 Toggle metric / imperial units (`u`)
- 🕘 Recent city history (`h` — last 5 searches)
- 🌈 Condition-based weather icons

---

## 🚀 Run

```bash
pip install requests
export OPENWEATHER_API_KEY="your_key_here"   # macOS/Linux
# set OPENWEATHER_API_KEY=your_key_here      # Windows

python weather.py
```

Get a free API key at [openweathermap.org](https://openweathermap.org/api).

---

## 💻 Commands

| Input | Action |
|---|---|
| `<city>` | Current weather for that city |
| `f <city>` | 3-day forecast |
| `u` | Toggle °C ↔ °F |
| `h` | Show recent searches |
| `q` | Quit |

---

## 💻 Demo

```
[°C] Enter city (or command): beirut

☁️  Beirut, LB
  🌡️  Temp      : 24°C  (feels like 26°C)
  💧 Humidity  : 68%
  🌬️  Wind      : 5.1 m/s W
  🌈 Condition : Partly cloudy
  🌅 Sunrise   : 05:47    🌇 Sunset: 19:32
```
