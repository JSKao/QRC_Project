# filepath: src/qrc/analysis/nmse.py
import numpy as np

def calculate_nmse(y_true, y_pred):
    """
    計算正規化均方誤差 (NMSE)
    NMSE = MSE / Var(y_true)
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    mse = np.mean((y_true - y_pred) ** 2)
    var = np.var(y_true)
    if var == 0:
        return np.nan
    return mse / var