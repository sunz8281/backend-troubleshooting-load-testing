from sqlalchemy import Column, Integer, String, Text
from app.database import Base


class Post(Base):
    """블로그 포스트 모델"""
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
