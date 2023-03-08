import pandas as pd
import os
from sqlalchemy import create_engine

DB_ENDPOINT = os.environ.get("DB_ENDPOINT")
DB_USERNAME = os.environ.get("DB_USERNAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")
DB_PORT = os.environ.get("DB_PORT", 5432)


def get_table():
    # Connect to database
    engine = create_engine(
        f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_ENDPOINT}:{DB_PORT}/{DB_NAME}"
    )

    return pd.read_sql_table("adjudications", engine)


def generate_report():
    # group by establishment, religion, offence and get count offence
    df = get_table()
    df1 = df.groupby(["Establishment", "Religion", "Offence"])["Offence"].count()
    df1.columns = ["Establishment", "Religion", "Offence", "Count"]
    return df1


def persist_data():
    #  Placeholder for when we want to save the data into a storage place.
    pass


def main():
    generate_report()


if __name__ == "__main__":
    main()
