import openai

# Get your API key from https://beta.openai.com/signup/
API_KEY = "Your API_KEY"

openai.api_key = (API_KEY)

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "What is the captial of India"}
  ]
)

print(response['choices'][0]['message']['content'])