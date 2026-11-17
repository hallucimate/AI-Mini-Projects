import requests
import os
from dotenv import load_dotenv
import json 



print("[INFO] The Program started.")

# -------------- LOAD THE API KEY AND VERIFY -----------------# 
load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    print("[INFO] No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
elif not api_key.startswith("sk-proj-"):
    print("[INFO] An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
else:
    print("[INFO] API key found.")





# ----------------- Craft the request to OPEN AI -------------___# 

prompt = "Tell me a fun fact"
print("[INFO] Prompt: " + prompt)

headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

payload = {
    "model": "gpt-6-luna",
    "reasoning_effort": "none",
    "messages": [
        {"role": "user", "content": prompt}
    ]
}

# Post the request:
response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers=headers,
    json=payload
)

# DEBUG: Get the whole response in json:
# print(response.json())

# DEBUG: Better way to display json using json package:
# print(json.dumps(response.json(), indent=4))

# Get only the message:
print("\n\n The content: \n")
print(response.json()["choices"][0]["message"]["content"])