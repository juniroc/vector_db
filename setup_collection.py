import os
import numpy as np
import DataType
from pymilvus import connections, db, CollectionSchema, Collection
from constants import fields


def initialize_database(self, database_name: str):
    if database_name not in db.list_databases():
        # create milvus database
        db.create_database(database_name)


def create_collection(collection_name: str) -> None:
    schema = CollectionSchema(fields, "temp collection")

    collection = Collection(name=collection_name, schema=schema)

    print(f"Collection '{collection_name}' created")


def insert_data(collection_name):
    # 벡터 데이터 생성

    collection = Collection(collection_name)
    entities = [
        vectors
    ]
    collection.insert(entities)
    print("Data inserted into collection")
