import unittest
from unittest import mock
import pytest
import math
from calculate_grades import *

def test_calculate_stat():
    grade_list = [16, 32, 47, 52, 88]
    mean, std_dev = calculate_stat(grade_list)
    assert mean == 47
    assert std_dev == math.sqrt(2)