# filepath: tests/test_parity_capacity.py
import numpy as np
from qrc.analysis.parity_capacity import calculate_pc

def test_calculate_pc_random():
    np.random.seed(0)
    x = np.random.rand(200)
    y = np.random.rand(200)
    pc = calculate_pc(x, y, max_delay=5)
    assert abs(pc) < 0.1

def test_calculate_pc_perfect():
    # y(t) = parity(x(t-1), x(t-2))
    x = np.random.randint(0, 2, 100)
    parity = np.bitwise_xor(x[:-2], x[1:-1])
    y = np.concatenate([[0, 0], parity])
    pc = calculate_pc(x, y, max_delay=2)
    assert pc >= 1.0