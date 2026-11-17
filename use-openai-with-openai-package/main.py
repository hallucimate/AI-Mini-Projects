import os
from dotenv import load_dotenv
from openai import OpenAI





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


prompt = "Tell me a fun fact"
print("[INFO] Prompt: " + prompt)

openai = OpenAI()

# Uses the older Chat Completions API 
response = openai.chat.completions.create(model="gpt-6-luna", reasoning_effort="none", messages=[{"role": "user", "content":  prompt}])

print("\n:::.. A fun fact provided by Open AI ..:::")
print(response.choices[0].message.content)