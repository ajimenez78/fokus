from datetime import datetime
from utils.timers import pomodoro_cycle
from utils.persistence import load_data, save_data

DATA_FILE = "data/journal.json"

def start_day():
    print("\n🌅 Welcome to Fokus - Morning Routine 🌅")
    today = datetime.today().strftime('%Y-%m-%d')
    data = load_data()

    intentions = []
    for i in range(1, 4):
        task = input(f"Enter key intention #{i} (or press Enter to skip): ").strip()
        if task:
            intentions.append(task)

    mode = input("\n📌 What focus mode for today? (pomodoro / sprint / deep blocks): ").strip().lower()
    data[today] = {
        "intentions": intentions,
        "mode": mode,
        "distractions": [],
        "achievements": [],
        "reflection": ""
    }

    save_data(data)
    print("\n✅ Intentions saved. You've got this!\n")

def run_focus_session():
    print("🎯 Starting a Pomodoro cycle (25 min focus, 5 min break)...")
    pomodoro_cycle()

def end_day():
    print("\n🌙 Evening Reflection - Let’s wrap up your day.\n")
    today = datetime.today().strftime('%Y-%m-%d')
    data = load_data()
    day_data = data.get(today, {})

    # Log achievements
    achievements = []
    for i in range(1, 4):
        ach = input(f"🎯 Achievement #{i} (press Enter to skip): ").strip()
        if ach:
            achievements.append(ach)

    # Daily reflection
    reflection = input("\n📝 Final thoughts or reflection for today: ").strip()

    # Save
    day_data["achievements"] = achievements
    day_data["reflection"] = reflection
    data[today] = day_data
    save_data(data)

    print("\n💾 Day saved. Great job showing up today 🙌\n")

if __name__ == "__main__":
    start_day()
    input("Press Enter to begin your first focus session...")
    run_focus_session()

    end = input("\nDo you want to wrap up your day now? (y/n): ").strip().lower()
    if end == "y":
        end_day()
