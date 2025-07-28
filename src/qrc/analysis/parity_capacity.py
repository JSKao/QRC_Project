# filepath: src/qrc/analysis/parity_capacity.py
import numpy as np

def calculate_pc(input_sequence, output_sequence, max_delay=10):
    """
    計算奇偶校驗容量 (PC)：
      PC = sum_{τ=1}^{max_delay} Corr^2(y(t), parity(x(t-1),...,x(t-τ)))
    其中 parity = x(t-1) xor x(t-2) xor ... xor x(t-τ)
    """
    input_sequence = np.asarray(input_sequence)
    output_sequence = np.asarray(output_sequence)
    N = len(input_sequence)
    pc = 0.0
    for τ in range(1, max_delay + 1):
        if N <= τ:
            break
        # 取 τ 個延遲輸入，計算 parity
        delayed_bits = np.array([input_sequence[i:N-τ+i] > 0.5 for i in range(τ)], dtype=int)
        parity = np.bitwise_xor.reduce(delayed_bits, axis=0)
        y_current = output_sequence[τ:]
        c = np.corrcoef(parity, y_current)[0, 1]
        if not np.isnan(c):
            pc += c**2
    return pc