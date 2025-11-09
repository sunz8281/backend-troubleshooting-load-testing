"""
데이터베이스 초기화 및 더미 데이터 생성 스크립트

실행 방법:
    python init_db.py
"""
from app.database import engine, SessionLocal, Base
from app.models import Post


def init_database():
    """데이터베이스 테이블 생성 및 더미 데이터 삽입"""
    print("📊 데이터베이스 테이블 생성 중...")
    Base.metadata.create_all(bind=engine)
    print("✅ 테이블 생성 완료")

    db = SessionLocal()
    try:
        # 기존 데이터가 있는지 확인
        existing_count = db.query(Post).count()
        if existing_count > 0:
            print(f"⚠️  기존 데이터 {existing_count}개가 존재합니다. 초기화를 건너뜁니다.")
            return

        # 100개의 더미 Post 생성
        print("🔄 더미 데이터 생성 중...")
        posts = []
        for i in range(1, 101):
            post = Post(
                title=f"블로그 포스트 #{i}",
                content=f"이것은 {i}번째 블로그 포스트의 내용입니다. "
                        f"라이브 코딩 발표를 위한 더미 데이터입니다."
            )
            posts.append(post)

        db.bulk_save_objects(posts)
        db.commit()
        print(f"✅ {len(posts)}개의 Post 생성 완료")

        # 결과 확인
        total_posts = db.query(Post).count()
        print(f"📝 총 Post 개수: {total_posts}")

    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    init_database()
