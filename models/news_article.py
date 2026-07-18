from dataclasses import dataclass

@dataclass(frozen=True)
class NewsArticle:
    title: str
    source: str
    published: str
    url: str
