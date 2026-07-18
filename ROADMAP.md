# Three-Eyed Raven Roadmap

Three-Eyed Raven is a learning-focused news agent that collects, evaluates, summarizes, and reports current news from multiple sources.

The initial priority is to build a small working prototype before adding frameworks, automation, or more complex agent behavior.

## v0.1 — Working News Summarizer

Goal: Produce a Markdown report from a small set of news articles.

* Fetch news from one RSS feed
* Filter articles by topic
* Select a limited number of articles
* Extract article metadata
* Summarize articles using an LLM
* Save the result as a Markdown report
* Add basic logging
* Handle failed requests without stopping the full run

### Completion criteria

The application can be started locally with one command and produces a readable report containing:

* Article title
* Source
* Publication date, when available
* Original article link
* Summary

## v0.2 — Basic Agent Workflow

Goal: Move from a fixed pipeline toward a goal-driven workflow.

* Accept a user-defined research topic
* Decide which articles are relevant
* Rank articles by estimated importance
* Remove obvious duplicate stories
* Track the actions taken during a run
* Verify that the final report was created successfully
* Produce a run summary

### Completion criteria

The agent can receive a goal such as:

> Find and summarize the most important AI news today.

It then selects, processes, and reports relevant articles without requiring step-by-step instructions.

## v0.3 — Memory

Goal: Prevent repeated coverage and retain useful information between runs.

* Store previously processed article URLs
* Store article titles and publication dates
* Skip previously summarized articles
* Detect similar stories from different sources
* Maintain lightweight local storage
* Add a configurable memory retention period

### Completion criteria

Running the agent on consecutive days does not repeatedly summarize the same articles unless meaningful new information is available.

## v0.4 — Multi-Source Research

Goal: Improve coverage and reduce dependence on one source.

* Support multiple RSS feeds
* Support configurable news sources
* Compare reporting across sources
* Prefer primary or authoritative sources where available
* Group articles covering the same event
* Include source attribution in the final report

### Completion criteria

The agent can combine several sources into one report while minimizing duplicate coverage.

## v0.5 — Research Mode

Goal: Support deeper investigation of a specific topic.

* Accept broader research questions
* Search for supporting sources
* Gather information from multiple articles
* Compare claims between sources
* Identify uncertainty or disagreement
* Generate a structured research report
* Include citations or source links

### Completion criteria

The agent can produce a coherent report for a request such as:

> Research the latest developments in humanoid robotics.

## v0.6 — Scheduled Execution

Goal: Run the agent automatically.

* Add scheduled local execution
* Support daily and weekly reports
* Create timestamped output files
* Maintain execution logs
* Prevent overlapping runs
* Add optional email or messaging delivery

### Completion criteria

The agent can run unattended on a schedule and deliver or save a report reliably.

## v0.7 — Configuration and Reliability

Goal: Make the application easier to operate and maintain.

* Move settings into configuration files or environment variables
* Add command-line arguments
* Add retries and request timeouts
* Add structured logging
* Add unit tests
* Add integration tests for external services
* Improve error reporting
* Add token and API cost controls

### Completion criteria

The application behaves predictably under common failure conditions and can be configured without editing source code.

## v1.0 — Stable Personal News Agent

Goal: Deliver a reliable, configurable, and useful news research workflow.

* Multiple topics and source profiles
* Relevance ranking
* Duplicate detection
* Persistent memory
* Scheduled execution
* Structured Markdown reports
* Reliable error handling
* Test coverage for core components
* Clear setup and usage documentation

## Possible Future Features

These are not part of the initial scope.

* Web interface
* Chat-based interaction
* Telegram or Discord integration
* Podcast or audio summaries
* Sentiment and trend analysis
* Company monitoring
* Security advisory monitoring
* Multi-agent workflows
* Vector database integration
* Cloud deployment
* Model provider abstraction
* Human approval before selected actions

## Current Focus

The current focus is **v0.1**.

The project should remain deliberately small until the complete workflow below works reliably:

```text
Fetch news
    ↓
Select relevant articles
    ↓
Summarize
    ↓
Generate Markdown report
```
