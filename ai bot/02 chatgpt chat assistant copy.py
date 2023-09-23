import openai

openai.api_key = "YOUR_API_KEY"  # Replace with your actual OpenAI API key

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while True:
    user_input = input()
    if user_input.lower() == "quit()":
        break
    
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response.choices[0].message.content # type: ignore
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
