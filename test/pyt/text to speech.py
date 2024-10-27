import pyttsx3


def speak_text(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume (1 is max, 0 is min)

    # Select voice (0 for male, 1 for female if available)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Change to voices[0].id for male

    # Speak the text
    engine.say(text)
    engine.runAndWait()  # Blocks while processing all currently queued commands


if __name__ == "__main__":
    while True:
        # Take user input
        user_input = input("Please enter the text you want to speak (type 'stop', 'quit', or 'exit' to end): ")

        # Check for exit commands
        if user_input.lower() in ['stop', 'quit', 'exit']:
            print("Exiting the program. Goodbye!")
            break

        # Call the function to speak the text
        speak_text(user_input)
