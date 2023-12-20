import pandas as pd


def get_data(table_name, connection):
    return pd.read_sql(f"SELECT * FROM {table_name}", connection)
