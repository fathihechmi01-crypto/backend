from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    reservations = relationship("Reservation", back_populates="user")


class Seance(Base):
    __tablename__ = "seances"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String)
    heure = Column(String)
    coach = Column(String)
    capacite = Column(Integer)

    reservations = relationship("Reservation", back_populates="seance")


class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    seance_id = Column(Integer, ForeignKey("seances.id"))

    user = relationship("User", back_populates="reservations")
    seance = relationship("Seance", back_populates="reservations")