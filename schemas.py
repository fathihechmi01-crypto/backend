from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class SeanceCreate(BaseModel):
    date: str
    heure: str
    coach: str
    capacite: int

class ReservationCreate(BaseModel):
    seance_id: int