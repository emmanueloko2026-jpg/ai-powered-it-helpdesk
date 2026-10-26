from fastapi import FastAPI, HTTPException
from backend.models import TicketCreate
from backend.store import tickets
from backend.services import find_ticket_by_id
from backend.services import save_ticket
from backend.services import resolve_ticket_service

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/tickets")
def get_tickets():
    return tickets

@app.get("/tickets/{ticket_id}")
def get_ticket(ticket_id: int):
    ourTicket = find_ticket_by_id(ticket_id)
    if ourTicket == None:
        raise HTTPException(status_code = 404, detail = "Ticket not found")
    return ourTicket


@app.post("/tickets")
def create_ticket(ticket: TicketCreate):
    userTicket = ticket.model_dump()
    result = save_ticket(userTicket)
    return result



@app.patch("/tickets/{ticket_id}")
def resolve_ticket(ticket_id: int):
    reResult = resolve_ticket_service(ticket_id)
    if reResult is None:
        raise HTTPException(status_code = 404, detail = "Ticket not found")
    elif reResult == "Ticket already resolved":
        raise HTTPException(status_code = 409, detail = "Ticket already resolved")
    return {"message": "Ticket resolved successfully", "ticket": reResult}