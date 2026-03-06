import pytest
from pipeline import transform, validate


def test_transform_removes_empty_amounts():
    rows = [
        {'id': '1', 'name': 'Alice', 'amount': '100'},
        {'id': '2', 'name': 'Bob', 'amount': ''},
        {'id': '3', 'name': 'Carol', 'amount': '250'},
    ]
    result = transform(rows)
    assert len(result) == 2


def test_transform_strips_whitespace():
    rows = [
        {'id': '1', 'name': '  Alice  ', 'amount': '100'},
    ]
    result = transform(rows)
    assert result[0]['name'] == 'Alice'


def test_validate_accepts_valid_amount():
    rows = [{'id': '1', 'name': 'Alice', 'amount': '100'}]
    # should not raise
    validate(rows)


def test_validate_handles_invalid_amount():
    rows = [{'id': '1', 'name': 'Bob', 'amount': 'not-a-number'}]
    # should not raise — validate prints a warning, doesn't crash
    validate(rows)
