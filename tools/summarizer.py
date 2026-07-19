import os
from typing import Optional

from openai import OpenAI, OpenAIError


DEFAULT_MODEL = "gpt-5-mini"
MAX_ARTICLE_CHARACTERS = 20_000


class ArticleSummaryError(Exception):
    """Raised when an article cannot be summarized."""


def summarize_article(
    title: str,
    article_text: str,
    model: Optional[str] = None,
) -> str:
    """
    Summarize an article using an OpenAI model.

    Args:
        title: The article title.
        article_text: Extracted article body text.
        model: Optional model override.

    Returns:
        A concise article summary.

    Raises:
        ValueError: If required input is empty.
        ArticleSummaryError: If configuration or API execution fails.
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
        response = client.responses.create(
            model=selected_model,
            instructions=(
                "You are a precise news summarizer. "
                "Use only information contained in the supplied article. "
                "Do not introduce outside facts or speculation."
            ),
            input=(
                f"Article title:\n{title}\n\n"
                f"Article text:\n{truncated_text}\n\n"
                "Write a concise summary containing:\n"
                "1. A two-to-three sentence overview.\n"
                "2. Three key points as bullet points.\n"
                "3. Why the story matters in one sentence.\n"
                "Clearly state when the article itself expresses uncertainty."
            ),
        )
    except OpenAIError as exc:
        raise ArticleSummaryError(
            f"OpenAI request failed: {exc}"
        ) from exc

    summary = response.output_text.strip()

    if not summary:
        raise ArticleSummaryError("The model returned an empty summary")

    return summary
