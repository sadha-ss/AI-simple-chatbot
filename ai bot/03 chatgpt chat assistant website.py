import openai
import gradio

openai.api_key = "YOUR_API_KEY"  # Replace with your actual OpenAI API key

# Set the initial system message
system_msg = "You are a real estate expert with knowledge in property investment and negotiation"
messages = [{"role": "system", "content": system_msg}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    chatbot_reply = new_func(response)[0]["message"]["content"] # type: ignore
    messages.append({"role": "assistant", "content": chatbot_reply})
    return chatbot_reply

def new_func(response):
    return response["choices"]

demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="Real Estate Pro")

demo.launch(share=True)
