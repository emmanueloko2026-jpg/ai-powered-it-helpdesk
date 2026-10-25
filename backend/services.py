from backend.store import tickets


def find_ticket_by_id(ticket_id):
    for ticket in tickets:
        if ticket["ticket_id"] == ticket_id:
            return ticket
    return None


def save_ticket(ticket):
    highest = 0
    if not tickets:
        ticket["ticket_id"] = 1001
    for ticket in tickets:
        if ticket["ticket_id"] > highest:
                highest = ticket["ticket_id"]
                ticket["ticket_id"] = highest + 1
        ticket["status"] = "Open"
        tickets.append(ticket)
        return {"message": "Ticket created successfully", "ticket": ticket}