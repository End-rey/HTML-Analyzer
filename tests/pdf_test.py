import os
import pytest
from parser.pdf import parse

@pytest.fixture
def test_files():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    return {
        'sample_pdf': os.path.join(test_dir, 'test_files', 'sample.pdf'),
        'invalid_file': os.path.join(test_dir, 'test_files', 'invalid.txt')
    }

def test_parse_valid_pdf(test_files):
    # Note: You'll need to create a sample.pdf in test_files directory
    result = parse(test_files['sample_pdf'])
    assert isinstance(result, str)
    assert len(result) > 0

def test_parse_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        parse('nonexistent.pdf')

def test_parse_invalid_file(test_files):
    # Note: You'll need to create an invalid.txt in test_files directory
    with pytest.raises(Exception):
        parse(test_files['invalid_file'])
