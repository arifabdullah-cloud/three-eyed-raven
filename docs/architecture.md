# Three-Eyed Raven Architecture

## Overview

Three-Eyed Raven is designed around a simple principle:

> Each component should have one clear responsibility.

Rather than placing all logic inside a single script, the application is organized into layers that separate data models, external integrations, orchestration, and output generation.

This architecture keeps the project easy to understand, test, extend, and maintain as new capabilities are added.

---

# High-Level Architecture

```text
                         main.py
                            │
                            ▼
                  Report Builder Service
                            │
         ┌──────────────────┼──────────────────┐
         │                  │                  │
         ▼                  ▼                  ▼
     RSS Tool         Reader Tool      Summarizer Tool
         │                  │                  │
         └──────────────────┼──────────────────┘
                            ▼
                         Data Models
                            │
                            ▼
                 (Future) Markdown Renderer
                            │
                            ▼
                     Generated Report
```

---

# Data Flow

The application currently follows a straightforward pipeline.

```text
RSS Feed
    │
    ▼
NewsArticle
    │
    ▼
ArticleContent
    │
    ▼
ArticleSummary
    │
    ▼
DailyReport
    │
    ▼
Markdown Report (planned)
```

Each stage transforms data into a richer representation without modifying previous stages.

---

# Architectural Principles

## 1. Models represent data

The `models` package defines the application's core data structures.

Models should:

* represent business data
* validate data where appropriate
* contain little or no business logic

Examples:

* NewsArticle
* ArticleSummary
* DailyReport

Models should not perform network requests or interact with external systems.

---

## 2. Tools perform one external capability

The `tools` package contains integrations with systems outside the application.

Each tool has one responsibility.

Examples include:

* retrieving RSS feeds
* downloading article content
* interacting with an LLM

Tools should not coordinate workflows or call unrelated tools.

---

## 3. Services orchestrate workflows

Services coordinate multiple tools to achieve a business objective.

A service represents a use case rather than an external integration.

For example, building a daily report requires:

* retrieving article content
* summarizing articles
* collecting successful results
* handling failures

The service coordinates these steps while each tool remains focused on its own responsibility.

---

## 4. Renderers generate output

Renderers convert application data into presentation formats.

Future renderers may include:

* Markdown
* HTML
* Email
* PDF
* JSON

Renderers should never fetch data or perform business logic.

Their only responsibility is presentation.

---

## 5. main.py is the application entry point

The responsibility of `main.py` is to:

* load configuration
* invoke application services
* handle top-level errors
* display execution progress

Business logic should remain outside of `main.py`.

---

# Repository Structure

| Directory    | Responsibility                                     |
| ------------ | -------------------------------------------------- |
| `models/`    | Application data structures.                       |
| `tools/`     | External integrations and system interactions.     |
| `services/`  | Business workflows that coordinate multiple tools. |
| `renderers/` | Output generation and presentation.                |
| `output/`    | Generated reports and artifacts.                   |
| `docs/`      | Project documentation.                             |

---

# Error Handling Strategy

Errors should be handled as close as possible to where they occur.

Individual components should raise meaningful exceptions.

Higher-level services decide whether execution should continue or stop.

For example, if one article cannot be summarized, the report should continue processing the remaining articles rather than failing completely.

---

# Current Architecture

Current workflow:

```text
Fetch RSS
    │
    ▼
Read article
    │
    ▼
Summarize article
    │
    ▼
Build DailyReport
```

---

# Planned Architecture

The next planned enhancement introduces report rendering.

```text
Fetch RSS
    │
    ▼
Read article
    │
    ▼
Summarize article
    │
    ▼
Build DailyReport
    │
    ▼
Render Markdown
    │
    ▼
Save Report
```

Longer term, an autonomous planning layer will coordinate these capabilities to support more advanced research and reporting workflows.

---

# Design Philosophy

Three-Eyed Raven is intentionally built incrementally.

Rather than introducing complex frameworks from the beginning, each capability is implemented independently and then composed into larger workflows.

The objective is to understand the fundamentals of agentic systems before introducing advanced concepts such as memory, planning, autonomous decision making, or multi-agent collaboration.
