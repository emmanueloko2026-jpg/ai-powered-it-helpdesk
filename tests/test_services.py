from backend.services import find_ticket_by_id
from backend import services


def test_find_existing_ticket():
    foundTick = find_ticket_by_id(1001)
    assert foundTick["ticket_id"] == 1001

def test_find_non_existing_ticket():
    foundTick = find_ticket_by_id(9999)
    assert foundTick is None

def test_save_ticket(monkeypatch):
    monkeypatch.setattr(services, "tickets", [])
    sample_Ticket = {"user": "John", "title": "Sample Ticket", "description": "This is a sample ticket."}
    services.save_ticket(sample_Ticket)
    assert sample_Ticket["ticket_id"] == 1001
    assert sample_Ticket["status"] == "Open"
    assert len(services.tickets) == 1

def test_resolve_ticket_service(monkeypatch):
    monkeypatch.setattr(services, "tickets", [{"ticket_id": 1001, "status": "Open"}])
    assert services.resolve_ticket_service(1001)["status"] == "Resolved"
    assert services.tickets[0]["status"] == "Resolved"

def test_resolve_already_resolved_ticket(monkeypatch):
    monkeypatch.setattr(services, "tickets", [])
    services.tickets.append({"ticket_id": 1001, "status": "Resolved"})
    result = services.resolve_ticket_service(1001)
    assert result == "Ticket already resolved"
    assert services.tickets[0]["status"] == "Resolved"

def test_resolve_non_existing_ticket(monkeypatch):
    monkeypatch.setattr(services, "tickets", [])
    result = services.resolve_ticket_service(9999)
    assert result is None
