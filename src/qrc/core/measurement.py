import numpy as np
from qutip import sigmaz, qeye, tensor

class QuantumMeasurement:
    def __init__(self, num_spins=5):
        self.num_spins = num_spins
        self.si = qeye(2)
        self.sz = sigmaz()

    def observable(self, i):
        operators = [self.si] * self.num_spins
        operators[i] = self.sz
        return tensor(operators)

    def measure_all(self, rho):
        return np.array([(self.observable(i) * rho).tr().real for i in range(self.num_spins)])

    def hilbert_schmidt_distance(self, rho_1, rho_2):
        diff = rho_1 - rho_2
        return np.sqrt((diff.dag() * diff).tr())