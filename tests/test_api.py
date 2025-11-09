"""
API 엔드포인트 테스트

주의: 이 테스트는 '기능'만 검증하며, '성능'은 검증하지 않습니다.
따라서 /v1/slow 엔드포인트가 2초가 걸리더라도 테스트는 통과합니다.
"""
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    """루트 엔드포인트 테스트"""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_get_posts_slow():
    """
    🐌 병목이 있는 엔드포인트 테스트

    - 기능만 검증 (상태 코드, 데이터 형식)
    - 성능은 검증하지 않음 → 2초가 걸려도 통과
    """
    response = client.get("/api/posts/v1/slow")

    # 상태 코드 검증
    assert response.status_code == 200

    # 응답 데이터 검증
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 100  # 100개의 Post가 반환되어야 함

    # 첫 번째 Post의 구조 검증
    if len(data) > 0:
        first_post = data[0]
        assert "id" in first_post
        assert "title" in first_post
        assert "content" in first_post


def test_get_posts_fast():
    """
    ⚡ 최적화된 엔드포인트 테스트
    """
    response = client.get("/api/posts/v2/fast")

    # 상태 코드 검증
    assert response.status_code == 200

    # 응답 데이터 검증
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 100

    # 첫 번째 Post의 구조 검증
    if len(data) > 0:
        first_post = data[0]
        assert "id" in first_post
        assert "title" in first_post
        assert "content" in first_post
