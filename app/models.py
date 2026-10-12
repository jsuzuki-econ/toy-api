from datetime import date

from pydantic import BaseModel


class Event(BaseModel):
    name: str
    event_date: date