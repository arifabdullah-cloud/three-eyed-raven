import os
from typing import Optional

from openai import OpenAI, OpenAIError

from models.article_summary import ArticleSummary


DEFAULT_MODEL = "gpt-5-mini"
MAX_ARTICLE_CHARACTERS = 20_000


class ArticleSummaryError(Exception):
    """Raised when an article cannot be summarized."""


def summarize_article(
    title: str,
    article_text: str,
    model: Optional[str] = None,
) -> ArticleSummary:
    """
    Summarize an article into a validated ArticleSummary object.

    Args:
        title: Article title.
        article_text: Extracted article body.
        model: Optional OpenAI model override.

    Returns:
        A validated ArticleSummary object.

    Raises:
        ValueError: If a required input is empty.
        ArticleSummaryError: If configuration, generation, or parsing fails.
    """
    if not title.strip():
        raise ValueError("title cannot be empty")

    if not article_text.strip():
        raise ValueError("article_text cannot be empty")

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ArticleSummaryError(
            "OPENAI_API_KEY is not configured in the environment"
        )

    selected_model = model or os.getenv("OPENAI_MODEL", DEFAULT_MODEL)
    truncated_text = article_text[:MAX_ARTICLE_CHARACTERS]

    client = OpenAI(api_key=api_key)

    try:
        response = client.responses.parse(
            model=selected_model,
            instructions=(
                "You are a precise news summarizer. "
                "Use only information contained in the supplied article. "
                "Do not introduce outside facts or speculation. "
                "Write for a busy technical professional. "
                "Keep the complete summary concise."
            ),
            input=(
                f"Article title:\n{title}\n\n"
                f"Article text:\n{truncated_text}"
            ),
            text_format=ArticleSummary,
        )
    except OpenAIError as exc:
        raise ArticleSummaryError(
            f"OpenAI request failed: {exc}"
        ) from exc

    summary = response.output_parsed

    if summary is None:
        raise ArticleSummaryError(
            "The model did not return a valid structured summary"
        )

    return summary
