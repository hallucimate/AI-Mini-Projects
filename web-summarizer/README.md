# Web Summarizer

A simple Python application that downloads a webpage, extracts its text using BeautifulSoup, and generates a concise summary using the OpenAI API.

## Requirements

- Python 3.10 or newer
- An OpenAI API key with API billing enabled

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/AI-Mini-Projects.git
cd AI-Mini-Projects/web-summarizer
```

Create and activate a Python virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install requests beautifulsoup4 openai python-dotenv
```

## Configuration

Create a `.env` file in the `web-summarizer` directory:

```dotenv
OPENAI_API_KEY=your-api-key-here
```

Never commit your actual API key to Git.

## Usage

Run the application:

```bash
python main.py
```

The application downloads the configured webpage and generates a three-bullet summary using OpenAI.

Currently, the target URL is defined directly in `main.py`.

## Technologies

Python, Requests, BeautifulSoup, OpenAI API, python-dotenv.