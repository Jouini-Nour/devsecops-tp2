from app import app


def client():
    return app.test_client()


def test_index():
    r = client().get("/")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"


def test_health():
    r = client().get("/health")
    assert r.status_code == 200


def test_get_user_found():
    r = client().get("/users/1")
    assert r.status_code == 200
    assert r.get_json()["name"] == "alice"


def test_get_user_not_found():
    r = client().get("/users/999")
    assert r.status_code == 404