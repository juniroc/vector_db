import os

from pymilvus import connections, db

from embedding import Embedding
import pandas as pd

conn =connections.connect(host="127.0.0.1", port=19530)


def main():
    directory_path = './'
    file_name = "question_answer_pairs.txt"
    file_path = os.path.join(directory_path, file_name)

    df = pd.read_csv(file_path, sep='\t')

    embedding = Embedding()
    result_dataframe = embedding.get_sentence_transformer_ef(df, 'Question')

if __name__ == "__main__":
    main()