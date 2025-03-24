# Data verification in CSV file

import pytest

@pytest.fixture()
def csv_data():
    with open('./test-data/book.csv') as f:
        data = f.read().split('\n')
    return data


def test_header_is_uppercase(csv_data):
    """Column names in header are upeprcase"""
    header = csv_data[0]
    assert header == header.upper()

def test_header_starts_with_id(csv_data):
    """First column in header is ID"""
    header = csv_data[0]
    column_names = header.split(',')
    first_column_name = column_names[0]
    assert first_column_name == 'ID'

def test_header_has_column_created(csv_data):
    """Header has column CREATED"""
    header = csv_data[0]
    column_names = header.split(',')
    assert 'CREATED' in column_names

def test_header_has_column_updated(csv_data):
    """Header has column UPDATED"""
    header = csv_data[0]
    column_names = header.split(',')
    assert 'UPDATED' in column_names

def test_record_matches_header(csv_data):
    """Number of columns in each record matches header"""
    header = csv_data[0]
    column_names = header.split(',')
    header_column_count = len(column_names)
    errors = []
    for record in csv_data[1:]:
        record_values = record.split(',')
        record_values_count = len(record_values)
        if record_values_count != header_column_count:
            errors.append(record)
    assert not errors

def test_record_first_field_is_number(csv_data):
    """First value in each record is number"""
    errors = []
    for record in csv_data[1:]:
        record_values = record.split(',')
        if not record_values[0].isdigit():
            errors.append(record)
    assert not errors

    