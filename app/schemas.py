from pydantic import BaseModel, ConfigDict


class PostRead(BaseModel):
    """Post 조회를 위한 Pydantic 스키마"""
    id: int
    title: str
    content: str

    model_config = ConfigDict(from_attributes=True)
