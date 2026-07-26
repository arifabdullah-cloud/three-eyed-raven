# Three-Eyed Raven

Three-Eyed Raven is a Python-based AI news reporting tool that automatically collects the latest Artificial Intelligence news from RSS feeds, extracts the main article content, summarises each article using an LLM, and generates a structured daily report in Markdown format.

The project is intended as a learning exercise in building AI-powered applications using clean software architecture, structured data models, and external APIs.

---

## Features

- Retrieve AI news from RSS feeds
- Extract article content from web pages
- Summarise articles using OpenAI GPT models
- Generate structured daily reports
- Export reports as Markdown
- Configuration through environment variables
- Modular architecture for future extension

---

## Project Structure

```
three-eyed-raven/
├── docs/
├── output/
├── src/
├── tests/
├── .env
├── .env.example
├── main.py
├── requirements.txt
└── README.md
```

---

## Architecture

```
RSS Feed
    │
    ▼
RSS Fetcher
    │
    ▼
Content Extractor
    │
    ▼
NewsArticle Models
    │
    ▼
Report Builder
    │
    ▼
OpenAI GPT
    │
    ▼
DailyReport Model
    │
    ▼
Markdown Renderer
    │
    ▼
output/YYYY-MM-DD-ai-report.md
```

---

## Requirements

- Python 3.9+
- OpenAI API Key

---

## Installation

Clone the repository.

```bash
git clone <repository-url>
cd three-eyed-raven
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

macOS/Linux

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file.

Example:

```env
OPENAI_API_KEY=your_api_key
OPENAI_MODEL=gpt-5-mini
```

Additional configuration options may be added as the project evolves.

---

## Usage

Run the application.

```bash
python main.py
```

A successful execution will:

1. Retrieve the latest AI news
2. Extract article content
3. Generate AI summaries
4. Produce a Markdown report

Reports are written to:

```
output/YYYY-MM-DD-ai-report.md
```

---

## Example Output

```
Artificial Intelligence Daily Report

Generated:
2026-07-26T02:35:38+00:00

Articles included: 5

1. Article Title

Source:
Published:
URL:

Overview
...
```

---

## Current Limitations

- Supports a single RSS source
- Reports are generated in Markdown only
- No historical storage
- No scheduling
- No duplicate article detection

---

## Roadmap

Planned improvements include:

- Multiple RSS sources
- HTML report generation
- Email delivery
- Report history
- Duplicate article detection
- Article categorisation
- Scheduled execution
- Additional output formats

---

## Learning Objectives

This project focuses on:

- Python application design
- AI integration
- Prompt engineering
- API consumption
- Structured data modelling
- Clean software architecture
- Software documentation

---

## License

This project is intended for learning and portfolio purposes.
