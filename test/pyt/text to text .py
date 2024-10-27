from groq import Groq

# Initialize the Groq client with your API key
api_key = "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"
client = Groq(api_key=api_key)


# Function to log input and output to a text file
def log_conversation(user_input, assistant_response, log_file="conversation_log.txt"):
    with open(log_file, "a") as f:
        f.write(f"You: {user_input}\n")
        f.write(f"Assistant: {assistant_response}\n\n")


# Main loop
if __name__ == "__main__":
    print("Welcome to the Text AI Assistant!")

    while True:
        # Take input from the user
        user_input = input("You: ")

        # Check for exit commands
        if user_input.lower() in ['stop', 'quit', 'exit']:
            print("Exiting the program. Goodbye!")
            break

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
                    "content": user_input
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

        # Log the conversation
        log_conversation(user_input, response_text)

        # Output the response
        print(f"Assistant: {response_text}")  # Print the response
