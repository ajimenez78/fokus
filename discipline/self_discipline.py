import json
import os
from datetime import datetime, date

FILE_PATH = "discipline/self_discipline_boost.json"

def load_boost_data():
    if not os.path.exists(FILE_PATH):
        print("Self-discipline module not initialized.")
        return None
    with open(FILE_PATH, "r") as f:
        return json.load(f)

def save_boost_data(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)

def calculate_week(start_date_str):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    today = datetime.today()
    delta_days = (today - start_date).days
    return min(4, delta_days // 7 + 1)

def maybe_advance_week(data):
    print(f"\nCurrent week: {data['week']}")
    next_week = input("Manually advance to next week? (y/n): ").lower()
    if next_week == 'y' and data["week"] < 4:
        data["week"] += 1
        save_boost_data(data)
        print(f"Advanced to week {data['week']}.")

def show_boost_routine():
    data = load_boost_data()
    if not data:
        return

    today = str(date.today())

    if "start_date" not in data:
        data["start_date"] = today

    data["week"] = calculate_week(data["start_date"])

    daily = data["daily_log"].get(today, {
        "victory_task": False,
        "focus_blocks_completed": 0,
        "distraction_limit_respected": False,
        "notes": ""
    })

    print("\n=== SELF-DISCIPLINE BOOST ===")
    print(f"Week {data['week']} - Daily Routine")
    print(f"Your WHY: {data['why']}")
    print(f"Victory Task: {data['victory_task']} [{'✅' if daily['victory_task'] else '❌'}]")
    print(f"Focus Blocks Target: {data['focus_blocks']} | Completed: {daily['focus_blocks_completed']}")
    print(f"Distraction Limit: {data['distraction_limit']} [{'✅' if daily['distraction_limit_respected'] else '❌'}]")
    print(f"Notes: {daily['notes']}")

    # Optional: update log if desired
    update = input("\nWould you like to update your progress for today? (y/n): ")
    if update.lower() == 'y':
        daily['victory_task'] = input("Did you complete the victory task? (y/n): ").lower() == 'y'
        daily['focus_blocks_completed'] = int(input("How many focus blocks did you complete?: "))
        daily['distraction_limit_respected'] = input("Did you respect your distraction limit? (y/n): ").lower() == 'y'
        daily['notes'] = input("Any notes about today?: ")

        data['daily_log'][today] = daily
        save_boost_data(data)
        print("Progress saved!")

    maybe_advance_week(data)

if __name__ == "__main__":
    show_boost_routine()
