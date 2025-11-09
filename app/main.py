from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db

app = FastAPI(
    title="Baseplate Blog API",
    description="라이브 코딩 발표용: 코드 레벨의 숨은 병목 찾아내기",
    version="1.0.0"
)


@app.get("/")
def read_root():
    """루트 엔드포인트"""
    return {
        "message": "Baseplate Blog API",
        "endpoints": {
            "slow": "/api/posts/v1/slow",
            "fast": "/api/posts/v2/fast"
        }
    }


@app.get("/api/posts/v1/slow", response_model=list[schemas.PostRead])
def get_posts_slow_endpoint(db: Session = Depends(get_db)):
    """
    🐌 병목이 있는 엔드포인트

    - 각 Post마다 time.sleep(0.02)를 호출
    - 100개의 Post가 있다면 약 2초 소요
    - pytest는 통과하지만 k6 부하 테스트는 실패할 것
    """
    return crud.get_posts_slow(db)


@app.get("/api/posts/v2/fast", response_model=list[schemas.PostRead])
def get_posts_fast_endpoint(db: Session = Depends(get_db)):
    """
    ⚡ 최적화된 엔드포인트

    - time.sleep() 없이 즉시 반환
    - 라이브 코딩에서 병목 해결 후 사용할 버전
    """
    return crud.get_posts_fast(db)
