import json
import os
from datetime import date

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

def show_boost_routine():
    data = load_boost_data()
    if not data:
        return

    today = str(date.today())
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

if __name__ == "__main__":
    show_boost_routine()
