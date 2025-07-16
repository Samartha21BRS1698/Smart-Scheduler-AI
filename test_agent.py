 # test_agent.py

# test_agent.py
from scheduler_agent import ask_agent
from calendar_utils import get_available_slots

import speech_recognition as sr
import pyttsx3

# Initialize speech recognizer and text-to-speech
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 180)  # speaking rate

def speak(text):
    print("Agent:", text)
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
    try:
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Speech recognition service unavailable.")
        return ""

def main():
    speak("SmartScheduler AI is ready! Say 'exit' to quit.")

    while True:
        try:
            user_input = listen().lower()
            if not user_input:
                continue

            if "exit" in user_input:
                speak("Goodbye!")
                break

            # Detect scheduling intent
            if "schedule" in user_input and "meeting" in user_input:
                speak("Checking your calendar for 1-hour slots on Tuesday afternoon.")
                slots = get_available_slots(duration_minutes=60, day='Tuesday', time_pref='afternoon')
                if slots:
                    speak("I found these available slots:")
                    for slot in slots:
                        speak(slot)
                else:
                    speak("No available slots found.")
                continue

            # Fallback to Gemini LLM
            response = ask_agent(user_input)
            speak(response)

        except KeyboardInterrupt:
            speak("Interrupted. Goodbye!")
            break
        except Exception as e:
            speak(f"Something went wrong: {str(e)}")

if __name__ == "__main__":
    main()
