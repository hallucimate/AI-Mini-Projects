import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from openai import OpenAI


# ------------- Use requests to work with HTTP requests -------------# 
response = requests.get("https://canadiancybersecuritynetwork.com/")
# DEBUG:
# print(response.status_code) 
# print(response.text) 


# ------------- Use Beautiful soup to extract text from HTML -------------# 
soup = BeautifulSoup(response.text, "html.parser")
text = soup.get_text(separator=" ", strip=True)
# soup.get_text() extracts text from all HTML elements, not just the title.
# separator=" " puts spaces between text fragments.
# strip=True removes leading and trailing whitespace from each fragment.

# print(text) # Debug



# ------------- Load API key from .env file -------------# 
load_dotenv()



# ------------- Use openai api -------------# 
client = OpenAI()

# use the new responsses API: https://api.openai.com/v1/responses
response_ai = client.responses.create(
    model="gpt-5-mini",
    instructions="Summarize the following webpage in 3 bullet points.",
    input=text
)

print(response_ai.output_text)


