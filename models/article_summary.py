from typing import List

from pydantic import BaseModel, Field


class ArticleSummary(BaseModel):
    overview: str = Field(
        description="A concise two-to-three sentence overview of the article."
    )
    key_points: List[str] = Field(
        description="Exactly three important points from the article.",
        min_length=3,
        max_length=3,
    )
    why_it_matters: str = Field(
        description="One concise sentence explaining why the story matters."
    )
