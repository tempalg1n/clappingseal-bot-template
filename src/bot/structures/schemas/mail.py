from typing import Optional

from pydantic import BaseModel, Field


class AttachedImage(BaseModel):
    name: str
    url: str


class ButtonSchema(BaseModel):
    text: str
    url: Optional[str] = None
    switch_inline_query: Optional[str] = None
    callback_data: Optional[str] = None

    class Config:
        from_attributes = True


class TelegramMailContent(BaseModel):
    image: Optional[AttachedImage] = Field(None)
    message_text: Optional[str]
    button: Optional[ButtonSchema] = Field(None)

    class Config:
        from_attributes = True


class TelegramMessage(TelegramMailContent):
    chat_id: int
    mailing_id: int
    user_id: int