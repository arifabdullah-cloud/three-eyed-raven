import os
import sys

from dotenv import load_dotenv

from models.news_article import NewsArticle
from tools.rss import RSSFeedError, fetch_articles
from services.report_builder import build_daily_report


DEFAULT_FEED_URL = "https://www.wired.com/feed/tag/ai/latest/rss"


def main() -> int:
    load_dotenv()

    feed_url = os.getenv("RSS_FEED_URL", DEFAULT_FEED_URL)
    max_articles = get_max_articles()

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
    
    print(f"\nExtracted {len(content.text)} characters.\n")
    print(content.text[:1000])
    print("\n[Output truncated]")

    print()
    print("=" * 60)
    print("Summarizing first article...")
    print("=" * 60)

    try:
        summary = summarize_article(
            title=articles[0].title,
            article_text=content.text,
        )
    except (ValueError, ArticleSummaryError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print()
    print("Overview:")
    print(summary.overview)

    print("\nKey points:")
    for point in summary.key_points:
        print(f"- {point}")

    print("\nWhy it matters:")
    print(summary.why_it_matters)
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
