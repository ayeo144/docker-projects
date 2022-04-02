from src.app import Base, engine, app

Base.metadata.create_all(bind=engine)