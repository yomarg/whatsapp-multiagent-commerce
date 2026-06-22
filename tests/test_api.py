import os
import pytest
from httpx import AsyncClient, ASGITransport
from src.api.main import app

os.environ["WHATSAPP_VERIFY_TOKEN"] = "test_token"

@pytest.mark.asyncio
async def test_verify_webhook_success():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/webhook/whatsapp", params={
            "hub.mode": "subscribe",
            "hub.challenge": "12345",
            "hub.verify_token": "test_token"
        })
    assert response.status_code == 200
    assert response.text == "12345"

@pytest.mark.asyncio
async def test_verify_webhook_fail():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/webhook/whatsapp", params={
            "hub.mode": "subscribe",
            "hub.challenge": "12345",
            "hub.verify_token": "wrong_token"
        })
    assert response.status_code == 403

@pytest.mark.asyncio
async def test_receive_webhook_malformed():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/webhook/whatsapp", json={"invalid": "payload"})
    assert response.status_code == 422
    assert "Traceback" not in response.text

@pytest.mark.asyncio
async def test_receive_webhook_success():
    payload = {
        "object": "whatsapp_business_account",
        "entry": [{
            "id": "123",
            "changes": [{
                "value": {
                    "messaging_product": "whatsapp",
                    "metadata": {"display_phone_number": "123", "phone_number_id": "123"},
                    "messages": [{
                        "from": "123456789",
                        "id": "wamid",
                        "text": {"body": "hola"},
                        "type": "text"
                    }]
                },
                "field": "messages"
            }]
        }]
    }
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/webhook/whatsapp", json=payload)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

@pytest.mark.asyncio
async def test_health_check():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "timestamp" in data
    assert "dependencies" in data
    assert data["status"] == "ok"
