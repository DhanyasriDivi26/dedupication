import pytest
from logging import ConsoleMessages

def sample_data():
    return {
        "id": "12345",
        "reasonForRemoval": "Duplicate entry"
    }

def test_append_reason(sample_data):
    updated_obj = ConsoleMessages.append_reason(sample_data, "Duplicate email")
    assert updated_obj["reasonForRemoval"] == "Duplicate email"

def test_summary_removed(capsys):
    ConsoleMessages.summary_removed('email')
    captured = capsys.readouterr()
    assert '\033[96m\n---------------DUPLICATE ENTRIES REMOVED!---------------\n' in captured.out
    assert 'The database contained duplicates for the following \033[91memail' in captured.out
    assert 'values.\nThose displayed were removed.' in captured.out

def test_greeting(capsys):
    ConsoleMessages.greeting()
    captured = capsys.readouterr()
    assert '\033[95m+++++=====+++++=====+++++\033[93m' in captured.out
    assert 'JSON DEDUPLICATION MACHINE' in captured.out

def test_files(capsys):
    ConsoleMessages.files()
    captured = capsys.readouterr()
    assert '\033[95m+++++=====+++++' in captured.out
    assert '\033[93mFILE OUTPUT' in captured.out

def test_duplicate_entry(capsys):
    ConsoleMessages.duplicate_entry('email', '2024-01-01', '2024-01-02', 'test@example.com')
    captured = capsys.readouterr()
    assert '----------Duplicate \033[91memail\033[96m value found: test@example.com----------' in captured.out
    assert '\033[92mentryDate of more recent _id: 2024-01-01' in captured.out
    assert '\033[91mentryDate of _id to be removed: 2024-01-02' in captured.out

def test_error_log(capsys):
    ConsoleMessages.error_log('processing data')
    captured = capsys.readouterr()
    assert 'An error occurred while \033[91mprocessing data\033[92m. Please check your resources and try again.' in captured.out