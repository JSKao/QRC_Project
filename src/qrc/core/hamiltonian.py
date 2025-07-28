import numpy as np
from qutip import sigmax, sigmaz, qeye, tensor, propagator

class TFIMHamiltonian:
    """
    Transverse-Field Ising Model Hamiltonian builder.
    """
    def __init__(self, num_spins=5, h=1.0, Js=1.0, seed=None):
        self.num_spins = num_spins
        self.h = h
        self.Js = Js
        if seed is not None:
            np.random.seed(seed)
        self.sx = sigmax()
        self.sz = sigmaz()
        self.si = qeye(2)

    def build(self):
        H = 0
        # Interaction part
        for i in range(self.num_spins):
            for j in range(i+1, self.num_spins):
                op_list = [self.si] * self.num_spins
                op_list[i] = self.sx
                op_list[j] = self.sx
                J = np.random.uniform(-self.Js/2, self.Js/2)
                H += J * tensor(op_list)
        # Transverse field part
        for i in range(self.num_spins):
            op_list = [self.si] * self.num_spins
            op_list[i] = self.sz
            H += self.h * tensor(op_list)
        return H

    def propagator(self, H, dt):
        return propagator(H, dt)