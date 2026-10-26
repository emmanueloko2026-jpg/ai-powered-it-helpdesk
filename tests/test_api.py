from fastapi.testclient import TestClient
from backend.main import app
from backend import main, services

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_get_nonexistent_ticket():
    response = client.get("/tickets/9999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Ticket not found"}

def test_create_ticket(monkeypatch):
    temporary_tickets = []
    monkeypatch.setattr(main, "tickets", temporary_tickets)
    monkeypatch.setattr(services, "tickets", temporary_tickets)
    ticket_data = {
        "user": "John",
        "title": "Sample Ticket",
        "description": "This is a sample ticket."
    }
    response = client.post("/tickets", json=ticket_data)
    assert response.status_code == 200
    assert response.json()["ticket"]["status"] == "Open"
    assert response.json()["message"] == "Ticket created successfully"


def test_resolve_ticket(monkeypatch):
    temp_tickets = [{
        "ticket_id": 1001,
        "status": "Open"
    }]
    monkeypatch.setattr(main, "tickets", temp_tickets)
    monkeypatch.setattr(services, "tickets", temp_tickets)
    patch_Given = client.patch("/tickets/1001")
    print(patch_Given.json())
    assert patch_Given.status_code == 200
    assert patch_Given.json()["ticket"]["status"] == "Resolved"
    assert temp_tickets[0]["status"] == "Resolved"

def test_resolve_already_resolved_ticket(monkeypatch):
    temp_tickets = [{
        "ticket_id": 1001,
        "status": "Resolved"
    }]
    monkeypatch.setattr(main, "tickets", temp_tickets)
    monkeypatch.setattr(services, "tickets", temp_tickets)
    patch_Given = client.patch("/tickets/1001")
    assert patch_Given.status_code == 409
    assert patch_Given.json() == {"detail": "Ticket already resolved"}
    assert temp_tickets[0]["status"] == "Resolved"

def test_create_ticket_missing_title(monkeypatch):
    temporary_tickets = []
    monkeypatch.setattr(main, "tickets", temporary_tickets)
    monkeypatch.setattr(services, "tickets", temporary_tickets)
    ticket_data = {
        "user": "John",
        "description": "This is a sample ticket without a title."
    }
    response = client.post("/tickets", json=ticket_data)
    assert response.status_code == 422  # Unprocessable Entity due to missing title
    assert temporary_tickets == []  # Ensure no ticket was created

def test_resolve_nonexistent_ticket(monkeypatch):
    temp_tickets = []
    monkeypatch.setattr(main, "tickets", temp_tickets)
    monkeypatch.setattr(services, "tickets", temp_tickets)
    patch_Given = client.patch("/tickets/9999")
    assert patch_Given.status_code == 404
    assert patch_Given.json() == {"detail": "Ticket not found"}
    assert temp_tickets == []  # Ensure no ticket was modified