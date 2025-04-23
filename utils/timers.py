import time

def countdown(minutes, label="Focus"):
    seconds = minutes * 60
    print(f"\n⏳ {label} session started ({minutes} min). Stay focused...\n")

    try:
        while seconds:
            mins, secs = divmod(seconds, 60)
            timeformat = f"{mins:02d}:{secs:02d}"
            print(f"\r{label} | {timeformat}", end="")
            time.sleep(1)
            seconds -= 1
        print(f"\n🔔 {label} session finished.\n")

    except KeyboardInterrupt:
        print(f"\n⚠️ {label} session interrupted.\n")

def pomodoro_cycle(focus_minutes=25, break_minutes=5):
    countdown(focus_minutes, label="Focus")
    input("Press Enter to start your break...")
    countdown(break_minutes, label="Break")
