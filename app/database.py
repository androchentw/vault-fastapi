from databases import Database
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from hvac import Client

DATABASE_URL = "postgresql://user:password@db:5432/testdb"
database = Database(DATABASE_URL)

metadata = MetaData()

example_table = Table(
    "example",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, index=True),
)

engine = create_engine(DATABASE_URL)
metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

VAULT_URL = "http://vault:8200"
vault = Client(url=VAULT_URL, token="your_vault_token")
