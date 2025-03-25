# Data verification in CSV file

# Import

import os
from typing import List, Union, Literal
import pytest


# Arrange
## Test data
def pytest_generate_tests(
    metafunc,
):
    """Dynamic parametrization test cases with CSV files in test-data directory."""
    test_data_dir = "./test-data/"

    if not os.path.exists(test_data_dir):
        pytest.fail(f"Test data directory does not exist: {test_data_dir}")

    csv_files = [
        os.path.join(test_data_dir, item) for item in os.listdir(test_data_dir) if item.endswith(".csv")
    ]  # Full path to CSV files

    if "csv_file" in metafunc.fixturenames:
        metafunc.parametrize("csv_file", csv_files)


# Act: Header Test Cases
@pytest.mark.CSVheader
class TestkHeaderSuite:

    def test_header_is_uppercase(self, csv_header: str):
        """Column names in header are upeprcase"""
        assert csv_header == csv_header.upper(), f"Header contains lowercase values: {csv_header}"

    def test_header_starts_with_id(self, column_names: List[str]):
        """First column in header is ID"""
        first_column_name = column_names[0]
        assert first_column_name == "ID", f"First comumn is '{column_names[0]}', expected 'ID'"

    @pytest.mark.parametrize("checked_name", ["CREATED", "UPDATED"])  # Checking param column names
    def test_header_has_column_name(
        self, column_names: List[str], checked_name: Union[Literal["CREATED"] | Literal["UPDATED"]]
    ):
        """Header has specific column name: CREATED/UPDATED"""
        assert checked_name in column_names, f"Missing expected column:{checked_name}"


# Act: Record Validation Test Cases
def test_record_matches_header(column_names: List[str], csv_records: List[str]):
    """Each record should have the same number of columns as header"""
    header_column_count = len(column_names)
    errors = []
    for record in csv_records:
        record_values = record.split(",")
        record_values_count = len(record_values)
        if record_values_count != header_column_count:
            errors.append(record)
    assert not errors, f"Records with incorrect column counts: {errors}"


def test_record_first_field_is_number(csv_records: List[str]):
    """First value in each record is number"""
    errors = []
    for record in csv_records:
        record_values = record.split(",")
        if not record_values[0].isdigit():
            errors.append(record)
    assert not errors, f"Records with non-numeric first fields: {errors}"
