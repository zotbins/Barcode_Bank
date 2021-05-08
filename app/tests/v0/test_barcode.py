from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from services.database import Base, get_db
from config import READ_API_KEY, WRITE_API_KEY
from main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///tests/v0/test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def test_post_barcode():
    response = client.post(
        "v0/barcode",
        json={
            "barcode": "12000009105",
            "item": "10200774 - MUG ROOT BEER",
            "bin": "Recycle",
        },
        headers={"X-API-KEY": WRITE_API_KEY},
    )
    assert response.status_code == 201
    assert response.json() == {
        "detail": "Barcode has been successfully added to the database"
    }


def test_post_barcode_bad_key():
    response = client.post(
        "v0/barcode",
        json={
            "barcode": "12412421",
            "item": "10200774 - MUG ROOT BEER",
            "bin": "Recycle",
        },
        headers={"X-API-KEY": "ABC"},
    )
    assert response.status_code == 401


def test_post_duplicate_barcode():
    response = client.post(
        "v0/barcode",
        json={
            "barcode": "12000009105",
            "item": "10200774 - MUG ROOT BEER",
            "bin": "Recycle",
        },
        headers={"X-API-KEY": WRITE_API_KEY},
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Barcode already exists in database"}


def test_get_barcode():
    response = client.get("v0/barcode/12000009105", headers={"X-API-KEY": READ_API_KEY})
    assert response.status_code == 200
    assert response.json() == {
        "barcode": "12000009105",
        "item": "10200774 - MUG ROOT BEER",
        "bin": "Recycle",
    }


def test_get_barcode_bad_key():
    response = client.get("v0/barcode/12000009105", headers={"X-API-KEY": "ABC"})
    assert response.status_code == 401


def test_get_nonexistent_barcode():
    response = client.get("v0/barcode/55", headers={"X-API-KEY": READ_API_KEY})
    assert response.status_code == 404
    assert response.json() == {"detail": "Barcode not found"}


def test_validation_error():
    response = client.get(
        "v0/barcode/5511111111111111111111111", headers={"X-API-KEY": READ_API_KEY}
    )
    assert response.status_code == 422
