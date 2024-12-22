import unittest
from datetime import datetime

from format import FormatUtils

from src.format import flatten_dict_values, deduplicate


def sample_data():
    return [
        {'_id': '1', 'email': 'test1@example.com', 'address': '123 Street','entryDate':datetime(2024, 1, 1)},
        {'_id': '2', 'email': 'test2@example.com', 'address': '456 Avenue','entryDate':datetime(2023, 1, 1)},
        {'_id': '1', 'email': 'test1@example.com', 'address': '123 Street','entryDate':datetime(2024, 2, 1)},  # Duplicate entry based on '_id'
        {'_id': '3', 'email': 'test3@example.com', 'address': '789 Road','entryDate':datetime(2024, 5, 1)},
        {'_id': '2', 'email': 'test2@example.com', 'address': '456 Avenue','entryDate':datetime(2024, 1, 1)}  # Duplicate entry based on 'email'
    ]

def test_format_array(sample_data):
    # Test FormatUtils.format_array
    formatted = FormatUtils.format_array(sample_data)
    assert isinstance(formatted, list)
    assert len(formatted) == 5  # Should return 5 items, as we are passing 5 items to format_array

def test_flatten_dict_values(sample_data):
    # Test flatten_dict_values
    data = {'key1': sample_data[:2], 'key2': sample_data[2:]}
    flattened = flatten_dict_values(data)
    assert len(flattened) == 5  # Should flatten all 5 items into a single list

def test_deduplicate(sample_data):
    # Test deduplication logic
    deduplicated_data, removed_entries = deduplicate(sample_data)
    
    # Check if the deduplicated data has no duplicates
    assert len(deduplicated_data) == 3  # Should be 3 after deduplication based on _id and email
    assert all(entry['email'] not in [e['email'] for e in deduplicated_data] for entry in deduplicated_data)  # No email duplicates
    
    # Check if removed entries are correct
    assert len(removed_entries) == 2  # Should contain the 2 removed entries based on duplicates
