import pandas as pd
import logging
import boto3


logging.basicConfig()
s3_client = boto3.client("s3")

# Input name for result of generate_report() transformation
report_name = "just_a_test"


def get_data(bucket: str, key: str) -> pd.DataFrame:
    response = s3_client.get_object(Bucket=bucket, Key=key)

    status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")

    if status == 200:
        logging.info("Data has been collected from {}/{}".format(bucket, key))
        return pd.read_csv(response.get("Body"))
    else:
        logging.error(
            "Bucket {} or file {} does not exist".format(bucket, key))
        raise


def generate_report(bucket: str, key: str) -> pd.DataFrame:
    # group by establishment, religion, offence and get count offence
    raw_data = get_data(bucket, key)
    transformed_data = raw_data.value_counts(
        subset=["Establishment", "Religion", "Offence"], sort=False).reset_index()
    transformed_data.columns = [
        "Establishment", "Religion", "Offence", "Count"]

    logging.info("Data is transformed")
    return transformed_data
