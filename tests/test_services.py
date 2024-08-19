import pytest
from app import services

@pytest.mark.asyncio
async def test_process_debt_records():
    data = [
        {"name": "John Doe", "governmentId": "1234567890", "email": "john@example.com", "debtAmount": 100.0, "debtDueDate": "2024-12-31", "debtID": "123e4567-e89b-12d3-a456-426614174000"}
    ]
    await services.process_debt_records(data)
    assert len(services.debt_records) == 1
    assert services.debt_records[0].name == "John Doe"
