import os
import sys

from dotenv import load_dotenv

from models.news_article import NewsArticle
from services.report_builder import build_daily_report
from tools.rss import RSSFeedError, fetch_articles


DEFAULT_FEED_URL = "https://www.wired.com/feed/tag/ai/latest/rss"


def main() -> int:
    load_dotenv()

    feed_url = os.getenv("RSS_FEED_URL", DEFAULT_FEED_URL)
    max_articles = get_max_articles()

    print("=" * 60)
    print("Three-Eyed Raven")
    print("=" * 60)
    print("\nFetching latest AI news...\n")

    try:
        articles = fetch_articles(
            feed_url=feed_url,
            max_articles=max_articles,
        )
    except (ValueError, RSSFeedError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if not articles:
        print("No articles were found.")
        return 0

    print(f"Retrieved {len(articles)} article(s).\n")

    for position, article in enumerate(articles, start=1):
        print_article(position, article)

    print("=" * 60)
    print("Building daily report...")
    print("=" * 60)
    print()

    try:
        report = build_daily_report(
            topic="Artificial Intelligence",
            articles=articles,
        )
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print("=" * 60)
    print("Report completed")
    print("=" * 60)
    print(f"Topic: {report.topic}")
    print(f"Generated: {report.generated_at.isoformat()}")
    print(f"Successful summaries: {len(report.items)}")
    print()

    for position, item in enumerate(report.items, start=1):
        print(f"{position}. {item.article.title}")
        print(f"   Overview: {item.summary.overview}")
        print()

    return 0


def get_max_articles() -> int:
    raw_value = os.getenv("MAX_ARTICLES", "5")

    try:
        value = int(raw_value)
    except ValueError:
        print(
            f"Warning: Invalid MAX_ARTICLES value '{raw_value}'. Using 5.",
            file=sys.stderr,
        )
        return 5

    if value <= 0:
        print(
            "Warning: MAX_ARTICLES must be greater than zero. Using 5.",
            file=sys.stderr,
        )
        return 5

    return value


def print_article(position: int, article: NewsArticle) -> None:
    print(f"{position}. {article.title}")
    print(f"   Source: {article.source}")
    print(f"   Published: {article.published}")
    print(f"   URL: {article.url}")
    print()


if __name__ == "__main__":
    raise SystemExit(main())
