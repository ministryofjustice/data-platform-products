import pandas as pd
import logging
import boto3
logging.basicConfig()

# This is a temporary solution, see DLAB-33 and DLAB-34 for more details.
# DB_ENDPOINT = os.environ.get("DB_ENDPOINT")
# DB_USERNAME = os.environ.get("DB_USERNAME")
# DB_PASSWORD = os.environ.get("DB_PASSWORD")
# DB_NAME = os.environ.get("DB_NAME")
# DB_PORT = os.environ.get("DB_PORT", 5432)


# def get_table():
#    # Connect to database
#    logging.info("Connecting to database. endpoint: %s, username: %s, db_name: %s, db_port: %s",
#                 DB_ENDPOINT, DB_USERNAME, DB_NAME, DB_PORT)
#    engine = create_engine(
#        f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_ENDPOINT}:{DB_PORT}/{DB_NAME}"
#    )
#    logging.info("Created connection to data")
#
#    return pd.read_sql_table("adjudications", engine)

def get_data(bucket, key):
    # This is something that should be hidden from the product developer. They should just pass in the file/table name.
    # It's then the responsibility of the data platform to find this file and execute the transformation code.
    s3_client = boto3.client("s3")
    bucket = bucket
    key = key
    response = s3_client.get_object(Bucket=bucket, Key=key)

    status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")

    if status == 200:
        return pd.read_csv(response.get("Body"))
    else:
        logging.error("Bucket {} or file {}".format(bucket, key))
        raise


def generate_report(bucket, key):
    # group by establishment, religion, offence and get count offence
    raw_data = get_data(bucket, key)
    transformed_data = raw_data.value_counts(
        subset=["Establishment", "Religion", "Offence"], sort=False).reset_index()
    transformed_data.columns = [
        "Establishment", "Religion", "Offence", "Count"]

    logging.info("Data is transformed and can now be persisted somewhere")
    return transformed_data
