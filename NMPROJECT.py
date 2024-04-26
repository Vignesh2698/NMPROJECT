pip install openai==0.28
import openai

# Set up your OpenAI API key
openai.api_key = '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'

# Define a function to interact with the OpenAI API and generate responses
def generate_response(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

# Main function to run the chatbot
def main():
    print("Welcome to ChatGPT! Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("ChatGPT: Goodbye!")
            break
        
        response = generate_response(user_input)
        print("ChatGPT: " + response)

if __name__ == "__main__":
    main()

