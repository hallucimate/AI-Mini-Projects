# Use OpenAI Without the OpenAI Package

A simple Python program demonstrating how to interact with the OpenAI API **without installing the official OpenAI Python SDK**.

Instead, it uses the `requests` library to send HTTP requests directly to the OpenAI API.

## Requirements

- Python 3
- An OpenAI API key
- `requests` and `python-dotenv` packages

Install the dependencies:

```bash
pip install requests python-dotenv
```

## Setup

**1. Create a `.env` file** in the project directory:

```env
OPENAI_API_KEY=your_api_key_here
```

**2. Run the program:**

```bash
python main.py
```

Replace `main.py` with your Python script's filename.

## How It Works

### 1. Load the API Key

```python
load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")
```

- `load_dotenv()` reads environment variables from the `.env` file.
- `override=True` ensures values from `.env` take priority over existing environment variables.
- `os.getenv()` retrieves the API key.

The program also checks whether an API key exists and whether it starts with `sk-proj-`.

### 2. Define the Prompt

```python
prompt = "Tell me a fun fact"
```

This is the message we want to send to the AI model.

### 3. Prepare the HTTP Headers

```python
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
```

- `Authorization` authenticates the request using the API key.
- `Content-Type` tells the server that we're sending JSON data.

### 4. Build the Request Payload

```python
payload = {
    "model": "gpt-6-luna",
    "reasoning_effort": "none",
    "messages": [
        {"role": "user", "content": prompt}
    ]
}
```

The payload contains the model configuration and the conversation messages.

- `model`: Specifies which AI model to use. The model ID must be available to your API account.
- `reasoning_effort`: Controls the model's reasoning effort, where supported.
- `messages`: Contains the conversation history, including the user's prompt.

### 5. Send the HTTP POST Request

```python
response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers=headers,
    json=payload
)
```

The `requests.post()` function sends an HTTP POST request to the OpenAI Chat Completions endpoint.

The `json=payload` argument automatically serializes the Python dictionary into JSON.

### 6. Extract the AI Response

```python
print(response.json()["choices"][0]["message"]["content"])
```

The API returns a JSON response. We extract the generated text using:

- `response.json()` — Converts the JSON response into a Python dictionary.
- `["choices"][0]` — Selects the first generated response.
- `["message"]["content"]` — Retrieves the generated text.

### 7. Debugging the Response

To inspect the complete JSON response in a readable format:

```python
import json

print(json.dumps(response.json(), indent=4))
```

This is useful for understanding the API response structure and troubleshooting errors.

## Important Notes

- Never commit your `.env` file or API keys to GitHub. Add `.env` to `.gitignore`.
- OpenAI API usage may incur charges.
- The program currently uses a hardcoded prompt.
- The program does not yet handle HTTP errors, network failures, or invalid API responses.
- For production use, validate the response status before accessing `choices`.

## What This Project Demonstrates

This project provides hands-on experience with:

- HTTP requests and REST APIs
- API authentication using Bearer tokens
- Environment variables and secret management
- JSON serialization and parsing
- Working with the OpenAI API directly, without an SDK

## Future Improvements

- Accept prompts from user input.
- Add HTTP error handling and timeouts.
- Support multi-turn conversations.
- Allow model selection through environment variables.

---

**Purpose:** Learn how AI API integrations work under the hood by communicating directly with the OpenAI API using standard HTTP requests.