from datetime import datetime, timezone
from typing import List

from models.daily_report import DailyReport, ReportItem
from models.news_article import NewsArticle
from tools.reader import ArticleReadError, read_article
from tools.summarizer import ArticleSummaryError, summarize_article


def build_daily_report(
    topic: str,
    articles: List[NewsArticle],
) -> DailyReport:
    """
    Read and summarize a list of articles.

    Articles that cannot be read or summarized are skipped so that one
    failure does not terminate the entire report.
    """
    if not topic.strip():
        raise ValueError("topic cannot be empty")

    report = DailyReport(
        topic=topic.strip(),
        generated_at=datetime.now(timezone.utc),
    )

    for article in articles:
        print(f"Processing: {article.title}")

        try:
            content = read_article(article.url)
            summary = summarize_article(
                title=article.title,
                article_text=content.text,
            )
        except (
            ValueError,
            ArticleReadError,
            ArticleSummaryError,
        ) as exc:
            print(f"Skipped: {article.title}")
            print(f"Reason: {exc}")
            print()
            continue

        report.items.append(
            ReportItem(
                article=article,
                summary=summary,
            )
        )

        print("Completed.")
        print()

    return report
