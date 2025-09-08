from pydantic import BaseModel, Field
from datetime import datetime


class Event(BaseModel):
    """Schema for the Event data"""

    id : str = Field(description="A unique id")
    title: str = Field(description="The title of the event.")
    time: datetime = Field(description="The time from when the event is palned.")



events = {}

