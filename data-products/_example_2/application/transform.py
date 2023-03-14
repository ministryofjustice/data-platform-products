import pandas as pd
import os
from sqlalchemy import create_engine
import logging

logging.basicConfig()

# This is a temporary solution, see DLAB-33 and DLAB-34 for more details.
DB_ENDPOINT = os.environ.get("DB_ENDPOINT")
DB_USERNAME = os.environ.get("DB_USERNAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")
DB_PORT = os.environ.get("DB_PORT", 5432)


def get_table():
    # Connect to database
    logging.info("Connecting to database. endpoint: %s, username: %s, db_name: %s, db_port: %s",
                 DB_ENDPOINT, DB_USERNAME, DB_NAME, DB_PORT)
    engine = create_engine(
        f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_ENDPOINT}:{DB_PORT}/{DB_NAME}"
    )
    logging.info("Created connection to data")

    return pd.read_sql_table("adjudications", engine)


def generate_report():
    # group by establishment, religion, offence and get count offence
    raw_data = get_table()
    transformed_data = raw_data.groupby(["Establishment", "Religion", "Offence"])[
        "Offence"].count()
    transformed_data.columns = [
        "Establishment", "Religion", "Offence", "Count"]

    logging.info("Data is transformed and can now be persisted somewhere")
    return transformed_data


def persist_data():
    #  Placeholder for when we want to save the data into a storage place.
    pass


def main():
    generate_report()


if __name__ == "__main__":
    main()
