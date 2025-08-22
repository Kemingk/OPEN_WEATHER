import os
from openai import OpenAI
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("not found OPENAI_API_KEY")

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"), ###你的_Duke_LiteLLM_API_KEY
    base_url="https://litellm.oit.duke.edu"
    )

# Call the Chat Completion endpoint
response = client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user",   "content": "Hello! How are you today?"}
    ]
)

# Extract and print the assistant's reply
reply = response.choices[0].message.content
print("ChatGPT says:", reply)