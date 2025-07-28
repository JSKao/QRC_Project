# filepath: src/qrc/analysis/memory_capacity.py
import numpy as np

def calculate_stm(input_sequence, output_sequence, max_delay=10):
    """
    計算短期記憶容量 (STM):
      MC = sum_{τ=1}^{max_delay} Corr(y(t), x(t-τ))^2
    """
    input_sequence = np.asarray(input_sequence)
    output_sequence = np.asarray(output_sequence)
    N = len(input_sequence)
    stm = 0.0
    for τ in range(1, max_delay+1):
        if N <= τ:
            break
        x_delayed = input_sequence[:-τ]
        y_current = output_sequence[τ:]
        corr = np.corrcoef(x_delayed, y_current)[0,1]
        if not np.isnan(corr):
            stm += corr**2
    return stm