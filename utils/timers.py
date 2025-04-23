import time
from datetime import datetime
from utils.persistence import load_data, save_data

def countdown(minutes, label="Focus"):
    seconds = minutes * 60
    print(f"\n⏳ {label} session started ({minutes} min). Press 'd' + Enter to log a distraction.\n")

    start_time = time.time()
    end_time = start_time + seconds

    while time.time() < end_time:
        remaining = int(end_time - time.time())
        mins, secs = divmod(remaining, 60)
        print(f"\r{label} | {mins:02d}:{secs:02d}", end="", flush=True)
        time.sleep(1)

        # Check for distraction input without breaking loop
        try:
            from msvcrt import kbhit, getch  # Windows only
            if kbhit():
                key = getch().decode("utf-8").lower()
                if key == "d":
                    log_distraction()
        except ImportError:
            # For non-Windows systems, use fallback prompt
            if remaining % 60 == 0:
                answer = input("\nDid you get distracted? Type it (or press Enter to continue): ").strip()
                if answer:
                    log_distraction(answer)

    print(f"\n🔔 {label} session finished.\n")

def log_distraction(msg=None):
    if not msg:
        msg = input("\n🤯 What distracted you? ").strip()
    today = datetime.today().strftime('%Y-%m-%d')
    data = load_data()
    data.setdefault(today, {})
    data[today].setdefault("distractions", []).append(msg)
    save_data(data)
    print("📝 Distraction logged.\n")

def pomodoro_cycle(focus_minutes=25, break_minutes=5):
    countdown(focus_minutes, label="Focus")
    input("Press Enter to start your break...")
    countdown(break_minutes, label="Break")
