import pandas as pd
import logging
import boto3
import yaml
import os
from pathlib import Path


logging.basicConfig()
s3_client = boto3.client("s3")


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


def get_tables(bucket, key, source_data):
    yaml_key = os.path.join(
        "code/", key.split("/")[1], "extracted/metadata/02-data-dictionary.yml"
    )
    response = s3_client.get_object(Bucket=bucket, Key=yaml_key)
    data_dict = yaml.safe_load(response["Body"])
    tables_dict = {}
    for key in data_dict:
        tables_dict[key] = [
            i for i in data_dict[key]['tables']
            if data_dict[key]['tables'][i]['source_data'] == source_data
        ]

    return tables_dict


def generate_report(bucket: str, key: str) -> dict:
    results_dict = {}
    source_data = Path(key).parts[2]
    data_products_dict = get_tables(bucket, key, source_data)
    raw_data = get_data(bucket, key)
    for database, tables in data_products_dict.items():
        results_dict[database] = {}
        for table in tables:
            results_dict[database][table] = eval(
                table + "(bucket, key, raw_data)")

    return results_dict


# Add functions for each table transformation below


# function to create table 1
def adj_example_1(
    bucket: str,
    key: str,
    raw_data: pd.DataFrame
) -> pd.DataFrame:
    # group by establishment, religion, offence and get count offence
    transformed_data = raw_data.value_counts(
        subset=["Establishment", "Religion", "Offence"], sort=False).reset_index()
    transformed_data.columns = [
        "Establishment", "Religion", "Offence", "Count"]

    logging.info("Data is transformed")
    return transformed_data


# function to create table 2
def adj_example_2(
    bucket: str,
    key: str,
    raw_data: pd.DataFrame
) -> pd.DataFrame:

    transformed_data = raw_data.value_counts(
        subset=["Establishment"], sort=False).reset_index()
    transformed_data.columns = [
        "Establishment", "Count"]

    logging.info("Data is transformed")
    return transformed_data


def punishments_example_1(
    bucket: str,
    key: str,
    raw_data: pd.DataFrame
) -> pd.DataFrame:

    transformed_data = raw_data.value_counts(
        subset=["Establishment"], sort=False).reset_index()
    transformed_data.columns = [
        "Establishment", "Count"]

    logging.info("Data is transformed")
    return transformed_data
