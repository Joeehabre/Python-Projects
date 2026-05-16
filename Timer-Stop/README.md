# ⏱️ Timer & Stopwatch

A threaded terminal stopwatch (with lap times) and countdown timer (with human-readable duration input).

---

## ✨ Features

**Stopwatch**
- Live `HH:MM:SS` display that updates in real-time (threaded — never freezes)
- 🏁 Lap times — press `l` to record a lap
- ⏸️ Pause / resume
- Summary of all laps on stop

**Countdown Timer**
- Human-readable duration input: `90`, `1m30s`, `1h`, `2h30m` all work
- Live countdown display
- Pause / resume / cancel
- Alert when time's up

---

## 🚀 Run

```bash
python Timer-Stopwatch.py
```

No dependencies — stdlib only (`threading`, `time`).

---

## 💻 Commands

**Stopwatch**

| Key | Action |
|---|---|
| `l` | Record lap |
| `p` | Pause |
| `r` | Resume |
| `s` | Stop and show summary |

**Countdown**

| Key | Action |
|---|---|
| `p` | Pause |
| `r` | Resume |
| `c` | Cancel |

---

## 💻 Demo

```
⏱️  Timer & Stopwatch
  [1] Stopwatch
  [2] Countdown Timer
  [3] Exit

  ⏱  00:01:23

  🏁 Lap 1: 00:00:45
  🏁 Lap 2: 00:01:23

  ✅ Stopped — Total: 00:01:23
  📋 Lap times:
     Lap 1: 00:00:45
     Lap 2: 00:01:23
```
