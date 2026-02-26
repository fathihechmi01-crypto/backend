from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, auth
from database import engine, Base
from dependencies import get_db

app = FastAPI()

Base.metadata.create_all(bind=engine)

# REGISTER
@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = auth.hash_password(user.password)
    new_user = models.User(
        name=user.name,
        email=user.email,
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully"}

# LOGIN
@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()

    if not db_user or not auth.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = auth.create_access_token({"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}

# CREATE SEANCE
@app.post("/seance")
def create_seance(seance: schemas.SeanceCreate, db: Session = Depends(get_db)):
    new_seance = models.Seance(**seance.dict())
    db.add(new_seance)
    db.commit()
    return {"message": "Seance created"}

# GET SEANCES
@app.get("/seances")
def get_seances(db: Session = Depends(get_db)):
    return db.query(models.Seance).all()

# RESERVE SEANCE
@app.post("/reserve")
def reserve(res: schemas.ReservationCreate, db: Session = Depends(get_db)):
    new_res = models.Reservation(user_id=1, seance_id=res.seance_id)
    db.add(new_res)
    db.commit()
    return {"message": "Reservation successful"}