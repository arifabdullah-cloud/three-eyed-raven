from dataclasses import dataclass
from typing import Any

import feedparser
from models.news_article import NewsArticle

class RSSFeedError(Exception):
    """Raised when an RSS feed cannot be retrieved or parsed."""


def fetch_articles(feed_url: str, max_articles: int = 5) -> list[NewsArticle]:
    """
    Retrieve articles from an RSS feed.

    Args:
        feed_url: RSS feed URL.
        max_articles: Maximum number of articles to return.

    Returns:
        A list of NewsArticle objects.

    Raises:
        ValueError: If the input is invalid.
        RSSFeedError: If the feed cannot be retrieved or parsed.
    """
    if not feed_url.strip():
        raise ValueError("feed_url cannot be empty")

    if max_articles <= 0:
        raise ValueError("max_articles must be greater than zero")

    feed = feedparser.parse(feed_url)

    if feed.bozo and not feed.entries:
        error = getattr(feed, "bozo_exception", "Unknown RSS parsing error")
        raise RSSFeedError(f"Unable to parse RSS feed: {error}")

    source = _get_source_name(feed.feed)
    articles: list[NewsArticle] = []

    for entry in feed.entries[:max_articles]:
        title = _get_value(entry, "title", "Untitled article")
        url = _get_value(entry, "link", "")
        published = _get_value(
            entry,
            "published",
            _get_value(entry, "updated", "Publication date unavailable"),
        )

        if not url:
            continue

        articles.append(
            NewsArticle(
                title=title,
                source=source,
                published=published,
                url=url,
            )
        )

    return articles


def _get_source_name(feed_metadata: Any) -> str:
    return _get_value(feed_metadata, "title", "Unknown source")


def _get_value(data: Any, key: str, default: str) -> str:
    value = data.get(key, default)

    if value is None:
        return default

    return str(value).strip() or default
