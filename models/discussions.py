from pydantic import BaseModel
from typing import List

class Discussion(BaseModel):
    title: str
    selftext: str
    topComments: List[str]
    