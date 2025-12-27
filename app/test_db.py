# test_db.py
from sqlalchemy import create_engine

engine = create_engine("postgresql://mridulbagoria:Mridul91%40@localhost:5432/urlshortener")
engine.connect()
print("DB connected successfully!")
