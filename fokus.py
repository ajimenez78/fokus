import json
import os
from datetime import datetime

DATA_FILE = "data/journal.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

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

if __name__ == "__main__":
    start_day()
