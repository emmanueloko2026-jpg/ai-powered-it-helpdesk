
from pydantic import BaseModel


class TicketCreate(BaseModel):
    user : str
    title : str
    description : str
