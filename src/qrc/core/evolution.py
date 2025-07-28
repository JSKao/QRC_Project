import numpy as np
from qutip import basis, tensor

class QRCEvolution:
    def __init__(self, num_spins=5):
        self.num_spins = num_spins

    def inject_input(self, rho_current, input_value):
        s = input_value
        psi_inject = np.sqrt(1-s) * basis(2, 0) + np.sqrt(s) * basis(2, 1)
        rho_inject = psi_inject * psi_inject.dag()
        # 假設注入到第0個自旋
        rho_reduced = rho_current.ptrace(list(range(1, self.num_spins)))
        rho_new = tensor(rho_inject, rho_reduced)
        return rho_new

    def run(self, H, U, input_sequence, delta_t, dt):
        psi_current = tensor([basis(2, 0) for _ in range(self.num_spins)])
        rho_current = psi_current * psi_current.dag()
        rho_history = []
        input_times = []
        input_index = 0
        injection_interval = int(delta_t / dt)
        total_steps = len(input_sequence) * injection_interval
        for step in range(total_steps):
            if step % injection_interval == 0 and input_index < len(input_sequence):
                rho_current = self.inject_input(rho_current, input_sequence[input_index])
                input_times.append(step)
                input_index += 1
                rho_current = U * rho_current * U.dag()
                rho_history.append(rho_current)
            else:
                rho_current = U * rho_current * U.dag()
        return {
            'rho_history': rho_history,
            'input_times': input_times,
            'input_sequence': input_sequence
        }