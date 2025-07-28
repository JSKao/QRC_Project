import numpy as np
from qutip import basis, tensor, sigmax, sigmaz, qeye, propagator

from .hamiltonian import TFIMHamiltonian
from .measurement import QuantumMeasurement

class QRCSystem:
    def __init__(self, num_spins=5, h=1.0, Js=1.0, dt=0.025, seed=None):
        self.num_spins = num_spins
        self.h = h
        self.Js = Js
        self.dt = dt
        self.seed = seed
        self.ham = TFIMHamiltonian(num_spins, h, Js, seed)
        self.meas = QuantumMeasurement(num_spins)
        self.H = self.ham.build()
        self.U = propagator(self.H, self.dt)

    def run_trials(self, tlist, delta_t_list):
        Num_trials = len(delta_t_list)
        expectation_values = {i: {j: [] for j in range(self.num_spins)} for i in range(Num_trials)}
        distance_values = {i: [] for i in range(Num_trials)}
        x_values = {i: {j: [] for j in range(self.num_spins)} for i in range(Num_trials)}

        for trial_count, t in enumerate(delta_t_list):
            psi_current = tensor([basis(2, 0) for _ in range(self.num_spins)])
            psi_test = tensor([basis(2, 1) for _ in range(self.num_spins)])
            rho_current = psi_current * psi_current.dag()
            rho_test = psi_test * psi_test.dag()
            step_count = 0
            for _ in tlist:
                if step_count % int(t / self.dt) == 0:
                    s = np.random.uniform(0, 1)
                    psi_inject = np.sqrt(1-s) * basis(2, 0) + np.sqrt(s) * basis(2, 1)
                    rho_inject = psi_inject * psi_inject.dag()
                    rho_reduced = rho_current.ptrace(list(range(1, self.num_spins)))
                    rho_current = tensor(rho_inject, rho_reduced)
                    rho_test_reduced = rho_test.ptrace(list(range(1, self.num_spins)))
                    rho_test = tensor(rho_inject, rho_test_reduced)
                    rho_current = self.U * rho_current * self.U.dag()
                    rho_test = self.U * rho_test * self.U.dag()
                    for j in range(self.num_spins):
                        x_values[trial_count][j].append((self.meas.observable(j) * rho_current).tr())
                else:
                    rho_current = self.U * rho_current * self.U.dag()
                    rho_test = self.U * rho_test * self.U.dag()
                for j in range(self.num_spins):
                    expectation_values[trial_count][j].append((self.meas.observable(j) * rho_current).tr())
                distance_values[trial_count].append(self.meas.hilbert_schmidt_distance(rho_current, rho_test))
                step_count += 1
        return expectation_values, distance_values, x_values