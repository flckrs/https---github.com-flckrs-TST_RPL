from database import Base, engine
from models import Supply

print("Creating database ...")

Base.metadata.create_all(engine)