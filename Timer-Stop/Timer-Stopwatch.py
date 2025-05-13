# Created by Joe Habre
---

## ⏱️ **5. Timer & Stopwatch**

### 📁 Folder: `timer-stopwatch/timer.py`

```python
import time

def stopwatch():
    input("Press Enter to start the stopwatch...")
    start = time.time()
    input("Press Enter to stop...")
    end = time.time()
    print(f"⏱️ Elapsed Time: {round(end - start, 2)} seconds")

def countdown(seconds):
    print(f"⏳ Timer set for {seconds} seconds.")
    while seconds > 0:
        print(f"{seconds}...", end='\r')
        time.sleep(1)
        seconds -= 1
    print("⏰ Time's up!")

if __name__ == "__main__":
    print("1. Stopwatch\n2. Timer")
    choice = input("Choose mode: ")
    if choice == '1':
        stopwatch()
    elif choice == '2':
        sec = int(input("Enter time in seconds: "))
        countdown(sec)
    else:
        print("❌ Invalid choice.")
