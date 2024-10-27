import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import subprocess
import psutil  # To handle process termination
import time

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to make JARVIS speak with enhanced TTS
def jarvis_speak(text):
    # Set voice properties
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Change index for different voices
    engine.setProperty('rate', 150)  # Set speaking rate (words per minute)

    # Speak the text
    engine.say(text)
    engine.runAndWait()

# Function to recognize voice commands
def listen_command():
    with sr.Microphone() as source:
        jarvis_speak("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Adjust for ambient noise
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            jarvis_speak("Sorry, I didn't catch that. Could you repeat?")
            return ""
        except sr.RequestError as e:
            jarvis_speak("Could not request results from the speech recognition service.")
            print(f"Error: {e}")
            return ""

# Function to close applications
def close_application(app_name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == app_name:
            proc.terminate()  # You can use proc.kill() for force termination
            return True
    return False

# Function to perform tasks based on commands
def execute_command(command):
    print(f"Executing command: {command}")  # Debugging info
    if "open youtube" in command:
        jarvis_speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open whatsapp" in command:
        jarvis_speak("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")
    elif "open calendar" in command:
        jarvis_speak("Opening Calendar")
        os.startfile("C:\\Path\\To\\Your\\calendar.exe")  # Update with your calendar path
    elif "open instagram" in command:
        jarvis_speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
    elif "open brave" in command:
        jarvis_speak("Opening Brave")
        webbrowser.open("https://www.brave.com")
    elif "open twitter" in command or "open x" in command:
        jarvis_speak("Opening X (formerly Twitter)")
        webbrowser.open("https://www.twitter.com")
    elif "open paint" in command:
        jarvis_speak("Opening Paint")
        subprocess.Popen("mspaint.exe")
    elif "open chrome" in command:
        jarvis_speak("Opening Chrome")
        webbrowser.open("https://www.google.com")
    elif "search" in command and "youtube" in command:
        jarvis_speak("What would you like to search for on YouTube?")
        search_query = listen_command()
        if search_query:
            jarvis_speak(f"Searching for {search_query} on YouTube")
            webbrowser.open(f"https://www.youtube.com/results?search_query={search_query.replace(' ', '+')}")
    elif "open notepad" in command:
        jarvis_speak("Opening Notepad")
        subprocess.Popen("notepad.exe")
        time.sleep(2)  # Wait for Notepad to open
        jarvis_speak("What do you want to write in Notepad?")
        text_to_write = listen_command()
        if text_to_write:
            jarvis_speak("Writing your text in Notepad.")
            with open("note.txt", "w") as f:
                f.write(text_to_write)
            jarvis_speak("Your text has been written and saved as note.txt.")
    elif "open calculator" in command:
        jarvis_speak("Opening Calculator")
        subprocess.Popen("calc.exe")
    elif "open vs" in command or "open visual studio code" in command:
        jarvis_speak("Opening Visual Studio Code")
        vscode_path = "C:\\Path\\To\\Your\\Visual Studio Code"  # Update with your VSCode path
        subprocess.Popen(vscode_path)
    elif "close notepad" in command:
        jarvis_speak("Closing Notepad")
        close_application("notepad.exe")
    elif "close paint" in command:
        jarvis_speak("Closing Paint")
        close_application("mspaint.exe")
    elif "close chrome" in command:
        jarvis_speak("Closing Chrome")
        close_application("chrome.exe")
    elif "stop listening" in command or "exit" in command or "quit" in command or "stop" in command:
        jarvis_speak("Goodbye! Stopping all listening.")
        exit()  # Stop the program
    else:
        jarvis_speak("I'm not sure how to help with that.")

# Main loop
if __name__ == "__main__":
    jarvis_speak("Hello! I am JARVIS. How can I assist you today?")
    while True:
        command = listen_command()
        if command:
            execute_command(command)
