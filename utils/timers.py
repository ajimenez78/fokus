import time
import sys
import select
import os
from datetime import datetime
from utils.persistence import load_data, save_data

def play_sound():
    """Play a notification sound based on platform."""
    try:
        if sys.platform == 'win32':
            # Windows
            import winsound
            winsound.Beep(440, 1000)  # 440 Hz for 1 second
        elif sys.platform == 'darwin':
            # macOS
            os.system('afplay /System/Library/Sounds/Tink.aiff')
        else:
            # Linux/Unix
            # Check if any of these commands are available
            for cmd in ['paplay', 'aplay', 'play']:
                if os.system(f'which {cmd} > /dev/null 2>&1') == 0:
                    if cmd == 'paplay':
                        os.system('paplay /usr/share/sounds/freedesktop/stereo/complete.oga')
                    elif cmd == 'aplay':
                        os.system('aplay -q /usr/share/sounds/sound-icons/glass-water-1.wav')
                    elif cmd == 'play':
                        os.system('play -q /usr/share/sounds/sound-icons/glass-water-1.wav')
                    break
            else:
                # Fallback: Print bell character
                print('\a', end='', flush=True)
    except Exception:
        # Fallback in case of any issues
        print('\a', end='', flush=True)

def countdown(minutes, label="Focus"):
    seconds = minutes * 60
    print(f"\n⏳ {label} session started ({minutes} min). Press 'd' + Enter to log a distraction.\n")

    start_time = time.time()
    end_time = start_time + seconds

    while time.time() < end_time:
        remaining = int(end_time - time.time())
        mins, secs = divmod(remaining, 60)
        print(f"\r{label} | {mins:02d}:{secs:02d}", end="", flush=True)
        
        # Check if user pressed Enter to log distraction
        if check_for_input():
            user_input = input("\nPress 'd' + Enter to log a distraction (or any other key to continue): ").strip().lower()
            if user_input == 'd':
                log_distraction()
            print(f"\r{label} | {mins:02d}:{secs:02d}", end="", flush=True)
            
        time.sleep(1)

    # Play sound notification when timer ends
    play_sound()
    print(f"\n🔔 {label} session finished.\n")

def check_for_input():
    """Check if there's user input without blocking."""
    if sys.platform == 'win32':
        # Windows-specific approach
        try:
            from msvcrt import kbhit
            return kbhit()
        except ImportError:
            return False
    else:
        # Unix-like systems approach using select
        i, o, e = select.select([sys.stdin], [], [], 0.0001)
        for s in i:
            if s == sys.stdin:
                # Clear the input buffer
                sys.stdin.readline()
                return True
        return False

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
    play_sound()  # Play sound before asking to start break
    input("Press Enter to start your break...")
    countdown(break_minutes, label="Break")
    play_sound()  # Play sound when break ends too
