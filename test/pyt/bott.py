import speech_recognition as sr
from gtts import gTTS
import pygame
import os
import tempfile
import time
from groq import Groq

# Initialize the Groq client with your API key
api_key = "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"
client = Groq(api_key=api_key)

# Function to recognize speech
def recognize_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say your topic or question:")
        audio = recognizer.listen(source)  # Listen for the first phrase
        try:
            topic_of_interest = recognizer.recognize_google(audio)
            print(f"You said: {topic_of_interest}")
            return topic_of_interest
        except sr.UnknownValueError:
            speak("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError as e:
            speak(f"Could not request results from Google Speech Recognition service; {e}")
            return None

# Function to convert text to speech and play it
def speak(text):
    tts = gTTS(text=text, lang='en')
    # Create a temporary file for the audio response
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_audio_file:
        audio_file = temp_audio_file.name
        tts.save(audio_file)

    # Initialize Pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Control the loop speed

    pygame.mixer.quit()  # Clean up the Pygame mixer

    # Adding a delay before removing the file
    time.sleep(0.5)  # Wait for a short time before deleting the file
    try:
        os.remove(audio_file)  # Remove the file after playing
    except PermissionError:
        print("PermissionError: Trying to delete the file again.")
        time.sleep(1)  # Wait a moment before trying again
        try:
            os.remove(audio_file)  # Try deleting again
        except Exception as e:
            print(f"Could not delete file: {e}")

# Get the topic from audio input
speak("Please ask what you want.")
topic_of_interest = recognize_audio()

if topic_of_interest:  # Proceed only if the input was recognized
    # Create a chat completion request
    completion = client.chat.completions.create(
        model="llama3-groq-70b-8192-tool-use-preview",
        messages=[
            {
                "role": "system",
                "content": "You are an informative assistant. Provide detailed information on the topic."
            },
            {
                "role": "user",
                "content": topic_of_interest
            }
        ],
        temperature=0.5,
        max_tokens=1024,
        top_p=0.65,
        stream=True,
        stop=None,
    )

    # Prepare the response to speak
    response_text = ""
    for chunk in completion:
        response_text += chunk.choices[0].delta.content or ""

    # Speak the response
    speak(response_text)
