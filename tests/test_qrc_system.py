import numpy as np
from qrc.core.qrc_system import QRCSystem

def test_qrc_system_runs():
    tlist = np.linspace(0, 1, 10)
    delta_t_list = [0.1, 0.2]
    qrc = QRCSystem(num_spins=2, h=1, Js=1, dt=0.1, seed=42)
    expectation_values, distance_values, x_values = qrc.run_trials(tlist, delta_t_list)
    assert len(expectation_values) == len(delta_t_list)
    assert len(distance_values) == len(delta_t_list)