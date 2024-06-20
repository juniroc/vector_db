import DataType

from pymilvus import FieldSchema

fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, description="primary id"),
    FieldSchema(name="question", dtype=DataType.VARCHAR, description="Question"),
    FieldSchema(name="answer", dtype=DataType.VARCHAR, description="Question"),
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=128, description="vector")
    ]