import os

from pymilvus import connections, db

from embedding import Embedding
from utils import create_database


conn =connections.connect(host="127.0.0.1", port=19530)


import pandas as pd

directory_path = './'
file_name = "question_answer_pairs.txt"

file_path = os.path.join(directory_path, file_name)

df = pd.read_csv(file_path, sep='\t')

print(df.head())

embedding = Embedding()

result_dataframe = embedding.get_sentence_transformer_ef(df, 'Question')

print(result_dataframe.head())