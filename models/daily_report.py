from datetime import datetime
from typing import List

from pydantic import BaseModel, Field

from models.article_summary import ArticleSummary
from models.news_article import NewsArticle


class ReportItem(BaseModel):
    article: NewsArticle
    summary: ArticleSummary


class DailyReport(BaseModel):
    topic: str
    generated_at: datetime
    items: List[ReportItem] = Field(default_factory=list)
