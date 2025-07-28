# filepath: tests/test_nmse.py
import numpy as np
from qrc.analysis.nmse import calculate_nmse

def test_nmse_perfect():
    y = np.arange(10)
    assert calculate_nmse(y, y) == 0

def test_nmse_random():
    np.random.seed(0)
    y_true = np.random.randn(100)
    y_pred = np.random.randn(100)
    nmse = calculate_nmse(y_true, y_pred)
    assert nmse > 0