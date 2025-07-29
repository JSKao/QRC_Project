import numpy as np
from qutip import basis, tensor, sigmax, sigmaz, qeye, propagator

from .hamiltonian import TFIMHamiltonian
from .measurement import QuantumMeasurement

# noise model: depolarizing channel
def depolarizing_channel(rho, p):
    dims = rho.dims  # Get dimensions of the multi-qubit system
    d = rho.shape[0]
    return (1 - p) * rho + p * qeye(dims[0]) / d

class QRCSystem:
    def __init__(self, num_spins=5, h=1.0, Js=1.0, dt=0.025, seed=None, noise_p=0.0):
        self.num_spins = num_spins
        self.h = h
        self.Js = Js
        self.dt = dt
        self.seed = seed
        self.noise_p = noise_p
        self.ham = TFIMHamiltonian(num_spins, h, Js, seed)
        self.meas = QuantumMeasurement(num_spins)
        self.H = self.ham.build()
        self.U = propagator(self.H, self.dt)

    def run_trials(self, tlist, delta_t_list, input_seq=None):
        Num_trials = len(delta_t_list)
        expectation_values = {i: {j: [] for j in range(self.num_spins)} for i in range(Num_trials)}
        distance_values = {i: [] for i in range(Num_trials)}
        rho_histories = {i: [] for i in range(Num_trials)}
        x_values = {i: {j: [] for j in range(self.num_spins)} for i in range(Num_trials)}

        for trial_count, t in enumerate(delta_t_list):
            psi_current = tensor([basis(2, 0) for _ in range(self.num_spins)])
            psi_test = tensor([basis(2, 1) for _ in range(self.num_spins)])
            rho_current = psi_current * psi_current.dag()
            rho_test = psi_test * psi_test.dag()
            step_count = 0
            for _ in tlist:
                if step_count % int(t / self.dt) == 0:
                    if input_seq is not None:
                        s = input_seq[step_count]
                    else:
                        s = np.random.uniform(0, 1)
                    psi_inject = np.sqrt(1-s) * basis(2, 0) + np.sqrt(s) * basis(2, 1)
                    rho_inject = psi_inject * psi_inject.dag()
                    rho_reduced = rho_current.ptrace(list(range(1, self.num_spins)))
                    rho_current = tensor(rho_inject, rho_reduced)
                    rho_test_reduced = rho_test.ptrace(list(range(1, self.num_spins)))
                    rho_test = tensor(rho_inject, rho_test_reduced)
                    rho_current = self.U * rho_current * self.U.dag()
                    # if self.noise_p > 0, apply depolarizing noise
                    if self.noise_p > 0:
                        rho_current = depolarizing_channel(rho_current, p=self.noise_p)
                    rho_test = self.U * rho_test * self.U.dag()
                    for j in range(self.num_spins):
                        x_values[trial_count][j].append((self.meas.observable(j) * rho_current).tr())
                else:
                    rho_current = self.U * rho_current * self.U.dag()
                    rho_test = self.U * rho_test * self.U.dag()
                for j in range(self.num_spins):
                    expectation_values[trial_count][j].append((self.meas.observable(j) * rho_current).tr())
                distance_values[trial_count].append(self.meas.hilbert_schmidt_distance(rho_current, rho_test))
                # after updating rho_current
                rho_histories[trial_count].append(rho_current)
                step_count += 1
        return expectation_values, distance_values, x_values, rho_histories