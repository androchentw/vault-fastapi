from sqlalchemy import Column, Integer, String, MetaData, Table

metadata = MetaData()

example_table = Table(
    "example",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, index=True),
)
