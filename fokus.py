from daily import show_daily_routine
from discipline import show_boost_routine

if __name__ == "__main__":
    print("Welcome to Fokus!")
    print("Commands: routine, discipline, exit")

    while True:
        cmd = input("Enter command: ")
        if cmd == "routine":
            show_daily_routine()
        elif cmd == "discipline":
            show_boost_routine()
        elif cmd == "exit":
            break
        else:
            print("Unknown command.")
