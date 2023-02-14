import unittest
from unittest import mock
import pytest
import math
from calculate_grades import *

def test_calculate_stat():
    mean, std_dev = calculate_stat([47, 52, 32, 16, 88])
    assert math.isclose(mean, 79.7, abs_tol=0.01)
    assert math.isclose(std_dev, 19.89, abs_tol=0.01)