import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
api_key = "YOUR_API_KEY"
openai.api_key = api_key

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "What are some creative ways to use OpenAI's language models?"}]
)

print(completion.choices[0].message.content) # type: ignore
 