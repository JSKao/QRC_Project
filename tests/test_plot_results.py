# filepath: tests/test_plot_results.py
import numpy as np
from qrc.visualization.plot_results import plot_observables

def test_plot_observables_runs():
    tlist = np.linspace(0, 10, 20)
    expectation_values = [np.sin(tlist + i) for i in range(3)]
    try:
        plot_observables(tlist, expectation_values, 3)
    except Exception as e:
        assert False, f"Plotting failed: {e}"