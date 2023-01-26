from sqlmodel import create_engine, SQLModel

engine = create_engine("sqlite:///instance/app.db", echo=True, pool_pre_ping=True)
test_engine = create_engine("sqlite:///instance/test_app.db", echo=True, pool_pre_ping=True)