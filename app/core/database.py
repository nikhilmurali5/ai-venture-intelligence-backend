from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = (
    "postgresql://postgres:nikhil123@host.docker.internal:5432/venture_intelligence"
)
    #"postgresql://postgres:nikhil123@localhost:5432/venture_intelligence"


engine = create_engine(
    DATABASE_URL,
    echo=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()