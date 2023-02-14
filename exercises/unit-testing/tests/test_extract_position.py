import pytest
from extract_position import extract_position

def test_extract_position():
   assert float(extract_position('|Update| Positron location in particle accelerator is x:21.475'))

def test_extract_position_none():
    assert extract_position(0) == None
    assert extract_position('|Error| Positron location is undetermined') == None