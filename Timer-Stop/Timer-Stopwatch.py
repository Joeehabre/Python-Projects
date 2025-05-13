# Created by Joe Habre

import time
import sys

def format_time(seconds):
    return time.strftime('%H:%M:%S', time.gmtime(seconds))

def stopwatch():
    print("\n🕐 Stopwatch Started!")
    start = time.time()
    paused = False
    total_paused_time = 0
    pause_start = 0

    while True:
        print(f"Elapsed: {format_time(int(time.time() - start - total_paused_time))}", end='\r')
        time.sleep(1)

        if m := input("Press [p]ause / [r]esume / [s]top: ").lower().strip():
            if m == 'p' and not paused:
                paused = True
                pause_start = time.time()
                print("⏸️ Paused. Press 'r' to resume.")
            elif m == 'r' and paused:
                paused = False
                total_paused_time += time.time() - pause_start
                print("▶️ Resumed.")
            elif m == 's':
                total = int(time.time() - start - total_paused_time)
                print(f"\n✅ Final Time: {format_time(total)}")
                break

def timer():
    try:
        total_seconds = int(input("Enter countdown time in seconds: "))
    except ValueError:
        print("❌ Invalid input.")
        return

    print("⏳ Timer Started")
    while total_seconds:
        print(f"Time Left: {format_time(total_seconds)}", end='\r')
        time.sleep(1)
        total_seconds -= 1

    print("\n⏰ Time's up!")

def main():
    while True:
        print("\n⏱️ Timer & Stopwatch")
        print("1. Stopwatch")
        print("2. Countdown Timer")
        print("3. Exit")
        choice = input("Select an option: ").strip()

        if choice == '1':
            stopwatch()
        elif choice == '2':
            timer()
        elif choice == '3':
            print("👋 Exiting. Goodbye!")
            sys.exit()
        else:
            print("❌ Invalid selection.")

if __name__ == "__main__":
    main()
