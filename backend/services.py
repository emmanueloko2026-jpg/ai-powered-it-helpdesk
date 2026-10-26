from fastapi import HTTPException

from backend.store import tickets


def find_ticket_by_id(ticket_id):
    for ticket in tickets:
        if ticket["ticket_id"] == ticket_id:
            return ticket
    return None


def save_ticket(new_ticket):
    highest = 0
    if not tickets:
        new_ticket["ticket_id"] = 1001
    for ticket in tickets:
        if ticket["ticket_id"] > highest:
                highest = ticket["ticket_id"]
                new_ticket["ticket_id"] = highest + 1
    new_ticket["status"] = "Open"
    tickets.append(new_ticket)
    return {"message": "Ticket created successfully", "ticket": new_ticket}


def resolve_ticket_service(ticket_id):
    find_ticket = find_ticket_by_id(ticket_id)
    if find_ticket is None:
        return None
    if find_ticket["status"] == "Resolved":
        return "Ticket already resolved"
    else:
        find_ticket["status"] = "Resolved"
        return find_ticket