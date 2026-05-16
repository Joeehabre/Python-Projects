# 🗂️ Python Projects

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Projects](https://img.shields.io/badge/Projects-7-orange)

A collection of practical Python CLI tools and games — built to be actually useful, not just hello-world exercises.

---

## 📦 Projects

| Project | Description | Run |
|---|---|---|
| [🧮 Calculator](./calculator) | Terminal calculator with `ans` chaining, memory, full expression history | `python calculator.py` |
| [🐍 Snake Game](./snake-game) | Pygame snake with high score persistence, pause, and grid | `python snake.py` |
| [🌦️ Weather App](./weather-app) | Live weather + 3-day forecast via OpenWeatherMap API | `python weather.py` |
| [✅ To-Do List](./todo-list) | Task manager with priorities, due dates, search, and sort | `python todo.py` |
| [🔐 Password Generator](./PasswordGen) | Cryptographically secure generator with entropy score and batch output | `python PassGen.py` |
| [📏 Unit Converter](./UnitConverter) | Converts length, weight, temperature, speed, and volume | `python UnitConv.py` |
| [⏱️ Timer & Stopwatch](./Timer-Stop) | Threaded stopwatch with laps + countdown with human duration input | `python Timer-Stopwatch.py` |

---

## 🚀 Getting Started

**Requirements:** Python 3.8+

```bash
git clone https://github.com/Joeehabre/Python-Projects.git
cd Python-Projects
```

Install dependencies for the projects that need them:

```bash
pip install pygame        # Snake Game
pip install requests      # Weather App
pip install pyperclip     # Password Generator (optional — enables clipboard copy)
```

For the Weather App, set your API key before running:

```bash
export OPENWEATHER_API_KEY="your_key_here"   # macOS / Linux
set OPENWEATHER_API_KEY=your_key_here        # Windows
```

Get a free key at [openweathermap.org](https://openweathermap.org/api).

---

## 🛠️ Tech & Skills

| Area | Details |
|---|---|
| Language | Python 3 |
| GUI / Game | `pygame` |
| Networking | `requests`, REST APIs, JSON |
| Security | `secrets` module (CSPRNG) |
| Concurrency | `threading` (Timer/Stopwatch) |
| Storage | JSON file persistence |
| UX | Input validation, real-time display, color-coded output |

---

## 📁 Structure

```
Python-Projects/
├── calculator/          # calculator.py
├── snake-game/          # snake.py, highscore.json
├── weather-app/         # weather.py
├── todo-list/           # todo.py, tasks.json
├── PasswordGen/         # PassGen.py
├── UnitConverter/       # UnitConv.py
└── Timer-Stop/          # Timer-Stopwatch.py
```

---

## 🪪 License

MIT — use, modify, and learn from anything here freely.

---

## 🙋‍♂️ Author

**Joe Habre**
📧 [joehabre48@gmail.com](mailto:joehabre48@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/joe-habre-228557330)
📸 [Instagram](https://www.instagram.com/joeehabre)

---

> *"Code is a craft. These are my tools."*
