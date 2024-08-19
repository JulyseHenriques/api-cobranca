from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_csv():
    response = client.post("/upload-csv/", files={"file": ("test.csv", "name,governmentId,email,debtAmount,debtDueDate,debtID\nJohn Doe,1234567890,john@example.com,100.0,2024-12-31,123e4567-e89b-12d3-a456-426614174000")})
    assert response.status_code == 200
    assert response.json() == {"message": "CSV processed successfully"}

def test_generate_bills():
    response = client.post("/generate-bills/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bills generated and sent"}
