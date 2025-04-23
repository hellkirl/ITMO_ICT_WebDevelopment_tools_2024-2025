from sqlmodel import SQLModel, Session, create_engine
from models import models

db_url = "postgresql://user:Xce8ak6heDSH@localhost:5432/travel"
engine = create_engine(db_url, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
