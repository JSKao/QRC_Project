import numpy as np
from qrc.analysis.memory_capacity import calculate_stm

def test_calculate_stm():
    # 例子：線性序列延時 1 預期相關性 1 故 STM ≥ 1
    x = np.arange(100)
    y = np.roll(x, 1)
    stm_val = calculate_stm(x, y, max_delay=5)
    assert stm_val >= 1.0

def test_calculate_stm_random():
    np.random.seed(42)
    x = np.random.randn(200)
    y = np.random.randn(200)
    stm_val = calculate_stm(x, y, max_delay=5)
    # 隨機序列相關性應該接近 0
    assert abs(stm_val) < 0.1