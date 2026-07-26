# Architecture

## Overview

Three-Eyed Raven follows a linear processing pipeline. Each module has a single responsibility, making the application easier to understand, maintain, and extend.

---

## High-Level Flow

```
RSS Feed
    │
    ▼
tools/rss.py
    │
    ▼
tools/reader.py
    │
    ▼
tools/summarizer.py
    │
    ▼
services/report_builder.py
    │
    ▼
services/markdown_renderer.py
    │
    ▼
output/YYYY-MM-DD-ai-report.md
```

---

## Components

### `main.py`

Application entry point.

Initialises and executes the news reporting workflow.

---

### `agent.py`

Coordinates the application's end-to-end workflow by orchestrating the different components.

---

### `tools/rss.py`

Responsible for:

- Retrieving RSS feeds
- Parsing feed entries
- Creating article metadata

---

### `tools/reader.py`

Responsible for:

- Downloading article pages
- Extracting readable content
- Removing unnecessary HTML

---

### `tools/summarizer.py`

Responsible for:

- Preparing prompts
- Calling the configured OpenAI model
- Returning structured summaries

---

### `models/`

Contains the application's data models.

Current models include:

- `NewsArticle`
- `ArticleSummary`
- `DailyReport`

These models provide a structured representation of data throughout the processing pipeline.

---

### `services/report_builder.py`

Builds the final `DailyReport` by combining article metadata and generated summaries.

---

### `services/markdown_renderer.py`

Converts the completed `DailyReport` into Markdown and writes it to the `output` directory.

---

## Design Principles

### Separation of Concerns

Each module has a clearly defined responsibility.

### Modularity

Components can be modified or replaced independently with minimal impact on the rest of the application.

### Configurability

Application configuration is managed through environment variables rather than hardcoded values.

### Extensibility

The architecture supports future enhancements such as additional news sources, alternative LLM providers, new output formats, and scheduled execution.

---

## Future Enhancements

Potential future improvements include:

- Multiple RSS sources
- HTML report generation
- Email delivery
- Report history
- Duplicate article detection
- Scheduled execution
