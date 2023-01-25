from sqlmodel import create_engine, SQLModel

engine = create_engine("sqlite3:///instance/app.db", echo=True, pool_pre_ping=True)