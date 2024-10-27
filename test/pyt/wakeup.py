import pyaudio
import wave
import pyttsx3
import webbrowser
import os
import subprocess
import psutil
import time
import numpy as np

# Initialize the recognizer and text-to-speech engine
engine = pyttsx3.init()

# Function to make JARVIS speak
def jarvis_speak(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Change index for different voices
    engine.setProperty('rate', 150)  # Set speaking rate (words per minute)
    engine.say(text)
    engine.runAndWait()

# Function to record audio and detect the hotword
def listen_for_hotword():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    THRESHOLD = 500  # Threshold for detecting sound (can be adjusted)

    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    print("Listening for hotword...")

    while True:
        data = stream.read(CHUNK)
        audio_data = np.frombuffer(data, dtype=np.int16)

        # Simple hotword detection based on energy
        if np.abs(audio_data).mean() > THRESHOLD:
            # Hotword detected; break from the loop
            stream.stop_stream()
            stream.close()
            audio.terminate()
            return True

# Function to close applications
def close_application(app_name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == app_name:
            proc.terminate()  # Use proc.kill() for force termination
            return True
    return False

# Function to perform tasks based on commands
def execute_command(command):
    print(f"Executing command: {command}")
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
        # Here you would normally listen for the search query
    elif "open notepad" in command:
        jarvis_speak("Opening Notepad")
        subprocess.Popen("notepad.exe")
    elif "open calculator" in command:
        jarvis_speak("Opening Calculator")
        subprocess.Popen("calc.exe")
    elif "close notepad" in command:
        jarvis_speak("Closing Notepad")
        close_application("notepad.exe")
    elif "stop listening" in command or "exit" in command or "quit" in command or "stop" in command:
        jarvis_speak("Goodbye! Stopping all listening.")
        exit()
    else:
        jarvis_speak("I'm not sure how to help with that.")

# Main loop
if __name__ == "__main__":
    jarvis_speak("Hello! I am JARVIS. How can I assist you today?")
    while True:
        if listen_for_hotword():
            # When hotword detected, execute command
            jarvis_speak("Hotword detected. What can I do for you?")
            # Here you would normally listen for the command
