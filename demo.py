import datetime

class Reminder:
    def _init_(self, title, date_time):
        self.title = title
        self.date_time = date_time

def create_reminder():
    title = input("Enter the reminder title: ")
    date_str = input("Enter the date and time (YYYY-MM-DD HH:MM): ")
    date_time = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M')
    return Reminder(title, date_time)

def show_reminders(reminders):
    if not reminders:
        print("No reminders set.")
    else:
        print("Reminders:")
        for i, reminder in enumerate(reminders, start=1):
            print(f"{i}. {reminder.title} - {reminder.date_time.strftime('%Y-%m-%d %H:%M')}")

def main():
    reminders = []

    while True:
        print("\nReminder App")
        print("1. Create a reminder")
        print("2. Show reminders")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            reminder = create_reminder()
            reminders.append(reminder)
            print("Reminder created!")
        elif choice == '2':
            show_reminders(reminders)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if _name_ == "_main_":
    main()