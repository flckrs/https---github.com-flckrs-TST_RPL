from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine=create_engine("postgresql://postgres:GTA13579@localhost/supply_db",
  echo=True
)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)