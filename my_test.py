# Data verification in CSV file

#Import

import os
from typing import Any, Literal
import pytest

# Arrange
## Test data
def pytest_generate_tests(metafunc):    # Dynamic param for given directory, fail when directory is missing
    if not os.path.exists('./test-data/'):
        pytest.fail(f"Test data directory does not exist")  

    listing = os.listdir(path='./test-data/')
    csv_files = [os.path.join ('./test-data/', item) for item in listing if item.endswith('.csv')]  # Listed full path: parent folder + file .csv
    if 'csv_file' in metafunc.fixturenames:
        metafunc.parametrize('csv_file', csv_files)

## Fixtures
@pytest.fixture()   # Fixture for source files
def csv_data(csv_file):
    with open(csv_file) as f:
        data = f.read().split('\n')
    return data

@pytest.fixture()   # Fixture for header only
def csv_header(csv_data: list[str]):
    return csv_data[0]

@pytest.fixture()   # Fixture for records only
def csv_records(csv_data: list[str]):
    return csv_data[1:]

@pytest.fixture()   # Fixture for column names
def column_names(csv_header: Any):
    return csv_header.split(',')

# Act
def test_header_is_uppercase(csv_header: Any):
    """Column names in header are upeprcase"""
    assert csv_header == csv_header.upper()

def test_header_starts_with_id(column_names: Any):
    """First column in header is ID"""
    first_column_name = column_names[0]
    assert first_column_name == 'ID'

@pytest.mark.parametrize('checked_name', ['CREATED', 'UPDATED'])    # Checking param column names
def test_header_has_column_name(column_names: Any, checked_name: Literal['CREATED'] | Literal['UPDATED']):
    """Header has column name: CREATED/UPDATED"""
    assert checked_name in column_names

def test_record_matches_header(column_names: Any, csv_records: Any):
    """Number of columns in each record matches header"""
    header_column_count = len(column_names)
    errors = []
    for record in csv_records:
        record_values = record.split(',')
        record_values_count = len(record_values)
        if record_values_count != header_column_count:
            errors.append(record)
    assert not errors

def test_record_first_field_is_number(csv_records: Any):
    """First value in each record is number"""
    errors = []
    for record in csv_records:
        record_values = record.split(',')
        if not record_values[0].isdigit():
            errors.append(record)
    assert not errors
