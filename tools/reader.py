from dataclasses import dataclass

import trafilatura


@dataclass(frozen=True)
class ArticleContent:
    url: str
    text: str


class ArticleReadError(Exception):
    """Raised when an article cannot be downloaded or extracted."""


def read_article(url: str) -> ArticleContent:
    if not url.strip():
        raise ValueError("url cannot be empty")

    downloaded = trafilatura.fetch_url(url)

    if downloaded is None:
        raise ArticleReadError(f"Unable to download article: {url}")

    text = trafilatura.extract(
        downloaded,
        include_comments=False,
        include_tables=False,
        favor_precision=True,
    )

    if not text or not text.strip():
        raise ArticleReadError(f"Unable to extract article text: {url}")

    return ArticleContent(
        url=url,
        text=text.strip(),
    )
