import time
from sqlalchemy.orm import Session
from app.models import Post


def get_posts_slow(db: Session):
    """
    🐌 의도적인 성능 병목이 있는 함수

    N+1 또는 외부 API 호출을 시뮬레이션하기 위해
    각 Post마다 time.sleep()을 호출합니다.

    100개의 Post가 있다면: 100 * 0.02초 = 2초의 고정 지연
    """
    posts = db.query(Post).all()

    # 🔥 병목: 각 Post를 순회하며 20ms씩 지연
    for post in posts:
        time.sleep(0.02)  # 외부 API 호출이나 추가 DB 쿼리를 시뮬레이션

    return posts


def get_posts_fast(db: Session):
    """
    ⚡ 최적화된 함수 (라이브 코딩에서 구현할 버전)

    time.sleep() 없이 즉시 Post 목록을 반환합니다.
    """
    posts = db.query(Post).all()
    return posts
