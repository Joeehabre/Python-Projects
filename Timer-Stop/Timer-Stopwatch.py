# Created by Joe Habre
import time
import sys
import threading


def fmt(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


# ── Stopwatch ──────────────────────────────────────────────────────────────────

def stopwatch():
    print("\n🕐 Stopwatch")
    print("  Commands: [l]ap  [p]ause  [r]esume  [s]top\n")

    start = time.perf_counter()
    paused = False
    paused_at = 0.0
    total_paused = 0.0
    laps = []
    stop_event = threading.Event()

    def display():
        while not stop_event.is_set():
            if not paused:
                elapsed = time.perf_counter() - start - total_paused
                print(f"\r  ⏱  {fmt(elapsed)}   ", end="", flush=True)
            time.sleep(0.1)

    t = threading.Thread(target=display, daemon=True)
    t.start()

    while True:
        cmd = input().strip().lower()

        if cmd == "p" and not paused:
            paused = True
            paused_at = time.perf_counter()
            print("\n  ⏸  Paused")

        elif cmd == "r" and paused:
            nonlocal_paused_duration = time.perf_counter() - paused_at
            total_paused += nonlocal_paused_duration
            paused = False
            print("  ▶  Resumed")

        elif cmd == "l":
            elapsed = time.perf_counter() - start - total_paused
            lap_num = len(laps) + 1
            laps.append(elapsed)
            print(f"\n  🏁 Lap {lap_num}: {fmt(elapsed)}")

        elif cmd == "s":
            stop_event.set()
            elapsed = time.perf_counter() - start - total_paused
            print(f"\n\n  ✅ Stopped — Total: {fmt(elapsed)}")
            if laps:
                print("  📋 Lap times:")
                for i, lap in enumerate(laps, 1):
                    print(f"     Lap {i}: {fmt(lap)}")
            break


# ── Countdown Timer ────────────────────────────────────────────────────────────

def parse_duration(raw):
    raw = raw.strip()
    total = 0
    if "h" in raw or "m" in raw or "s" in raw:
        import re
        for value, unit in re.findall(r"(\d+)\s*([hms])", raw):
            mult = {"h": 3600, "m": 60, "s": 1}[unit]
            total += int(value) * mult
        return total
    return int(raw)


def countdown_timer():
    print("\n⏳ Countdown Timer")
    print("  Enter duration as seconds (e.g. 90) or using h/m/s (e.g. 1h30m or 2m30s)")

    try:
        raw = input("  Duration: ")
        total = parse_duration(raw)
        if total <= 0:
            raise ValueError
    except (ValueError, TypeError):
        print("❌ Invalid duration.")
        return

    stop_event = threading.Event()
    paused = threading.Event()

    print("  Commands: [p]ause  [r]esume  [c]ancel\n")

    def display():
        remaining = total
        last_tick = time.perf_counter()
        while remaining > 0 and not stop_event.is_set():
            if not paused.is_set():
                now = time.perf_counter()
                remaining -= now - last_tick
                last_tick = now
                display_time = max(0, remaining)
                print(f"\r  ⏳ {fmt(display_time)}   ", end="", flush=True)
            else:
                last_tick = time.perf_counter()
            time.sleep(0.1)

        if not stop_event.is_set() and remaining <= 0:
            print("\n\n  ⏰ Time's up!")
            stop_event.set()

    t = threading.Thread(target=display, daemon=True)
    t.start()

    while not stop_event.is_set():
        cmd = input().strip().lower()
        if cmd == "p":
            paused.set()
            print("\n  ⏸  Paused")
        elif cmd == "r":
            paused.clear()
            print("  ▶  Resumed")
        elif cmd == "c":
            stop_event.set()
            print("\n  🛑 Timer cancelled.")
            break

    t.join(timeout=0.5)


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    while True:
        print("\n⏱️  Timer & Stopwatch")
        print("  [1] Stopwatch")
        print("  [2] Countdown Timer")
        print("  [3] Exit")
        choice = input("  Select: ").strip()

        if choice == "1":
            stopwatch()
        elif choice == "2":
            countdown_timer()
        elif choice == "3":
            print("👋 Goodbye!")
            sys.exit()
        else:
            print("❌ Invalid selection.")


if __name__ == "__main__":
    main()
