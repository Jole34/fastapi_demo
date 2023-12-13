from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.setup import settings

engine = create_engine(settings.DB_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)