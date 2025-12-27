from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.db.model import URL
from app.schemas.url import URLCreate, URLResponse
from app.db.database import SessionLocal
from app.services.shortner import encode, decode
import os

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/shorten", response_model=URLResponse)
def shorten_url(payload: URLCreate, db: Session = Depends(get_db)):
    print("payload", payload)
    url = URL(long_url=str(payload.long_url))
    db.add(url)
    db.commit()
    db.refresh(url)

    short_code = encode(url.url_id)
    url.short_code = short_code
    db.commit()
    base_url = os.getenv("BASE_URL")
    return {"shortCode": f"{base_url}/{short_code}"}

@router.get("/{short_code}")
def redirect_to_url(short_code: str, db: Session = Depends(get_db)):
    url_id = decode(short_code)
    url = db.query(URL).filter(URL.url_id == url_id).first()
    
    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    
    return RedirectResponse(url=url.long_url, status_code=307)


