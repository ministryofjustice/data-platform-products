import boto3
import os
import pytest

from moto import mock_s3

aws_region = "eu-west-1"


# @pytest.fixture(scope="function")
# def aws_credentials():
#     """Mocked AWS Credentials for moto."""
#     os.environ["AWS_ACCESS_KEY_ID"] = "testing"
#     os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
#     os.environ["AWS_SECURITY_TOKEN"] = "testing"
#     os.environ["AWS_SESSION_TOKEN"] = "testing"
#     os.environ["AWS_DEFAULT_REGION"] = aws_region
@pytest.fixture(scope="module", autouse=True)
def tests_env_setup_and_teardown():

    TEMP_ENV_VARS = {
        "AWS_ACCESS_KEY_ID": 'testing',
        "AWS_SECRET_ACCESS_KEY": 'testing',
        "AWS_SECURITY_TOKEN": 'testing',
        "AWS_SESSION_TOKEN": 'testing',
        "AWS_DEFAULT_REGION": aws_region,
        "IAM_ROLE": "test_iam",
        "BOTO_CONFIG": "/dev/null"
    }

    # Will be executed before the first test
    old_environ = dict(os.environ)
    os.environ.update(TEMP_ENV_VARS)

    yield
    # # Will be executed after the last test
    # os.environ.clear()
    # os.environ.update(old_environ)


@pytest.fixture(scope="function")
def s3_mock_client():
    with mock_s3():
        conn = boto3.client("s3", region_name=aws_region)
        yield conn


# @pytest.fixture(scope="function")
# def s3_mock_resource(aws_credentials):
#     with mock_s3():
#         conn = boto3.resource("s3", region_name=aws_region)
#         yield conn
