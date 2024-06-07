import datetime

def set_reminder():
    speak("Para quando você quer definir o lembrete?")
    date_text = listen()
    try:
        reminder_date = datetime.datetime.strptime(date_text, "%d/%m/%Y").date()
        speak("Qual é o lembrete?")
        reminder_text = listen()
        with open("reminders.txt", "a") as file:
            file.write(f"{reminder_date.strftime('%d/%m/%Y')}: {reminder_text}\n")
        speak("Lembrete definido com sucesso.")
    except ValueError:
        speak("Formato de data inválido. Por favor, tente novamente.")

def check_reminders():
    today = datetime.date.today()
    with open("reminders.txt", "r") as file:
        reminders = file.readlines()
        for reminder in reminders:
            reminder_date_text, reminder_text = reminder.split(": ")
            reminder_date = datetime.datetime.strptime(reminder_date_text, "%d/%m/%Y").date()
            if reminder_date == today:
                speak(f"Lembrete para hoje: {reminder_text.strip()}")
