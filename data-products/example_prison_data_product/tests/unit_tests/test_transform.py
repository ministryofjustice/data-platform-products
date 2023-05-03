from application.transform import generate_report, get_tables
from unittest.mock import patch
import pandas as pd
import pytest
from pathlib import Path
import os


@pytest.fixture
def bucket_name():
    return "product-test-bucket"


@pytest.fixture(scope="function")
def s3_test_bucket(s3_mock_client, bucket_name):
    s3_mock_client.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={"LocationConstraint": "eu-west-1"}
    )
    yield


data1 = {"Date": ["Q3", "Q3", "Q3", "Q3"],
         "Outcomes": ["Dismissed", "Dismissed", "Dismissed", "Dismissed"],
         "Predominant function of establishment": ["Category A (High Security)", "Category B", "Category C",
                                                   "Local"],
         "Establishment": ["Belmarsh", "Belmarsh", "Frankland", "Frankland"],
         "Adjudicator": ["Governor", "Governor", "Governor", "Governor"],
         "Sex": ["M", "M", "M", "M"],
         "Age group": ["25 - 29", "30 - 39", "21 - 24", "30 - 39"],
         "Ethnicity": ["b Black/ African/ Caribbean/ Black British", "e White",
                       "c Mixed/ Multiple ethnic groups", "d Other ethnic group"],
         "Religion": ["b Muslim", "a Christian", "i No religion", "b Muslim"],
         "Offence": ["Disobedience/disrespect", "Disobedience/disrespect", "Unauthorised transactions",
                     "Unauthorised transactions"],
         "Detailed offence": ["Disobeys any lawful order", "Disobeys any lawful order", "Drug related offence",
                              "Drug related offence"],
         "Count": [1, 1, 1, 1]
         }


table_dict = {'product_for_test': ['adj_example_1']}


@patch('application.transform.get_data', return_value=pd.DataFrame.from_dict(data1))
@patch('application.transform.get_tables', return_value=table_dict)
def test_generate_report(mocked_data, mocked_tables):
    expected_data = {"Establishment": ["Belmarsh", "Belmarsh", "Frankland", "Frankland"],
                     "Religion": ["a Christian", "b Muslim", "b Muslim", "i No religion"],
                     "Offence": ["Disobedience/disrespect", "Disobedience/disrespect", "Unauthorised transactions",
                                 "Unauthorised transactions"],
                     "Count": [1, 1, 1, 1]}
    expected = pd.DataFrame.from_dict(expected_data)
    pd.testing.assert_frame_equal(
        generate_report(
            'fake_bucket',
            'product_for_test/test_table1/data.csv'
        )['product_for_test']['adj_example_1'],
        expected
    )


def test_get_tables(s3_mock_client, s3_test_bucket):
    s3_mock_client.upload_file(
        os.path.join(
            Path(__file__).parent.absolute(),
            "test_metadata",
            "02-data-dictionary.yaml"
        ),
        'product-test-bucket',
        "code/product_for_test/extracted/metadata/02-data-dictionary.yml"
    )

    expected_tables = {'product_for_test': ['test_table1']}

    tables = get_tables(
        bucket='product-test-bucket',
        key='raw_data/product_for_test/test_table1/data.csv',
        source_data='test1'
    )
    assert tables == expected_tables
