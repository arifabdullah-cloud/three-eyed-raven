from pydantic import BaseModel


class NewsArticle(BaseModel):
    title: str
    source: str
    published: str
    url: str
