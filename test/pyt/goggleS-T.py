import speech_recognition as sr
from gtts import gTTS
import pygame
import os
import tempfile
import time

# Initialize pygame for audio playback
pygame.mixer.init()

def speak(text):
    """Convert text to speech and play it."""
    tts = gTTS(text=text, lang='en')
    with tempfile.NamedTemporaryFile(delete=True) as temp_file:
        tts.save(temp_file.name)
        pygame.mixer.music.load(temp_file.name)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # wait for speech to finish
            time.sleep(1)

def recognize_speech_from_mic():
    """Recognize speech from the microphone."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please say something...")
        recognizer.adjust_for_ambient_noise(source)  # adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        # Use Google Web Speech API to recognize speech
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return "Sorry, I could not understand the audio."
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "Could not request results from Google Speech Recognition service."

if __name__ == "__main__":
    recognized_text = recognize_speech_from_mic()
    speak(recognized_text)  # Speak the recognized text
