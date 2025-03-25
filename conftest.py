import pytest
from typing import Any

## Fixtures


@pytest.fixture()  # Fixture for source files
def csv_data(csv_file):
    with open(csv_file) as f:
        data = f.read().split("\n")
    return data


@pytest.fixture()  # Fixture for header only
def csv_header(csv_data: list[str]):
    return csv_data[0]


@pytest.fixture()  # Fixture for records only
def csv_records(csv_data: list[str]):
    return csv_data[1:]


@pytest.fixture()  # Fixture for column names
def column_names(csv_header: Any):
    return csv_header.split(",")
