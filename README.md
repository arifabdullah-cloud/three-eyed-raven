# Three-Eyed Raven

Three-Eyed Raven is a Python-based AI news reporting application that automatically collects the latest Artificial Intelligence news from RSS feeds, extracts article content, summarises each article using an LLM, and generates a structured daily report in Markdown format.

The project serves as a practical exercise in building AI-powered applications using modular software design, structured data models, and external APIs.

---

## Features

- Retrieve AI news from RSS feeds
- Extract article content from web pages
- Summarise articles using OpenAI GPT models
- Generate structured daily reports
- Export reports in Markdown format
- Configurable using environment variables
- Modular architecture for future enhancements

---

## Project Structure

```text
three-eyed-raven/
├── docs/
├── models/
├── output/
├── services/
├── tools/
├── ROADMAP.md
├── agent.py
├── main.py
└── requirements.txt
```

### Directory Overview

| Directory | Purpose |
|-----------|---------|
| `docs/` | Project documentation |
| `models/` | Data models used throughout the application |
| `services/` | Business logic and report generation |
| `tools/` | Components for RSS retrieval, article extraction and summarisation |
| `output/` | Generated Markdown reports |

---

## Architecture

```
RSS Feed
    │
    ▼
RSS Reader
    │
    ▼
Article Reader
    │
    ▼
OpenAI Summariser
    │
    ▼
Report Builder
    │
    ▼
Markdown Renderer
    │
    ▼
Daily Report (.md)
```

---

## Requirements

- Python 3.9 or later
- OpenAI API Key

---

## Installation

Clone the repository.

```bash
git clone <repository-url>
cd three-eyed-raven
```

Create and activate a virtual environment.

macOS / Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file.

```env
OPENAI_API_KEY=your_api_key
OPENAI_MODEL=gpt-5-mini
```

---

## Usage

Run the application.

```bash
python main.py
```

The application will:

1. Retrieve the latest AI news
2. Extract article content
3. Generate AI summaries
4. Build a daily report
5. Save the report as a Markdown file

Generated reports are written to:

```text
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

Current limitations include:

- Single RSS feed
- Markdown output only
- No report history
- No scheduling
- No duplicate article detection

---

## Roadmap

See [ROADMAP.md](ROADMAP.md) for planned features and future improvements.

---

## Learning Objectives

This project focuses on:

- Python application design
- AI integration
- Prompt engineering
- API consumption
- Structured data modelling
- Software architecture
- Technical documentation

---

## License

This project is intended for learning and portfolio purposes.
