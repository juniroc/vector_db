import os

from pymilvus import db

MILVUS_HOST = os.getenv("MILVUS_HOST", "127.0.0.1")
MILVUS_PORT = os.getenv("MILVUS_PORT", 19530)


# create milvus database
def create_database(database_name: str):
    database = db.create_database(database_name)
    return database


