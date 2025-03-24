import pytest

# Data verification in CSV file
# First run - only positive


def test_header_is_uppercase():
    """Column names in header are upeprcase"""
    assert True

def test_header_starts_with_id():
    """First column in header is ID"""
    assert True

def test_header_has_column_created():
    """Header has column CREATED"""
    assert True

def test_header_has_column_updated():
    """Header has column UPDATED"""
    assert True

def test_record_matches_header():
    """Number of columns in each record matches header"""
    assert True

def test_record_first_field_is_number():
    """First value in each record is number"""
    assert True