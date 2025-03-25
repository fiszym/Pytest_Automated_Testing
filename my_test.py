# Data verification in CSV file

import pytest

@pytest.fixture(params=['./test-data/address.csv', './test-data/book.csv', './test-data/customer.csv'])
def csv_data(request):
    with open(request.param) as f:
        data = f.read().split('\n')
    return data

@pytest.fixture()
def csv_header(csv_data):
    return csv_data[0]

@pytest.fixture()
def csv_records(csv_data):
    return csv_data[1:]

@pytest.fixture()
def column_names(csv_header):
    return csv_header.split(',')

def test_header_is_uppercase(csv_header):
    """Column names in header are upeprcase"""
    assert csv_header == csv_header.upper()

def test_header_starts_with_id(column_names):
    """First column in header is ID"""
    first_column_name = column_names[0]
    assert first_column_name == 'ID'

@pytest.mark.parametrize('checked_name', ['CREATED', 'UPDATED'])
def test_header_has_column(column_names, checked_name):
    """Header has column name: CREATED/UPDATED"""
    assert checked_name in column_names

def test_record_matches_header(column_names, csv_records):
    """Number of columns in each record matches header"""
    header_column_count = len(column_names)
    errors = []
    for record in csv_records:
        record_values = record.split(',')
        record_values_count = len(record_values)
        if record_values_count != header_column_count:
            errors.append(record)
    assert not errors

def test_record_first_field_is_number(csv_records):
    """First value in each record is number"""
    errors = []
    for record in csv_records:
        record_values = record.split(',')
        if not record_values[0].isdigit():
            errors.append(record)
    assert not errors

    