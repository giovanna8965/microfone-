import speech_recognition as sr
import pyttsx3
import weather
import reminders

def listen():
    recognizer = sr.Recognizer()
    with Microphone() as source:
        print("Diga algo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language='pt-BR')
        print("Você disse: ", text)
        return text
    except sr.UnknownValueError:
        print("Não foi possível entender a fala.")
        return ""
    except sr.RequestError as e:
        print("Erro ao se comunicar com o serviço de reconhecimento de fala: {0}".format(e))
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    speak("Olá, eu sou o seu assistente de voz. Como posso ajudá-lo?")
    while True:
        command = listen().lower()

        if "parar" in command:
            speak("Até logo!")
            break
        elif "tempo" in command:
            speak("De qual cidade você quer saber o tempo?")
            city = listen()
            weather_info = weather.get_weather(city)
            speak(weather_info)
        elif "lembrete" in command:
            reminders.set_reminder()
        elif "verificar lembretes" in command:
            reminders.check_reminders()
        else:
            speak("Desculpe, não entendi. Você pode repetir?")

if __name__ == "__main__":
    main()
