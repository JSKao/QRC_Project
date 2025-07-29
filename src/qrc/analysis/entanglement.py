import numpy as np

def von_neumann_entropy(rho):
    eigvals = rho.eigenenergies()
    return -np.sum([v * np.log2(v) for v in eigvals if v > 0])

def purity(rho):
    return np.real((rho * rho).tr())

def global_entanglement(rho, num_spins):
    """
    Meyer-Wallach global entanglement Q.
    Q = 2/N * sum_i (1 - Tr(rho_i^2)), where rho_i is the reduced density matrix of qubit i.
    """
    Q = 0
    for i in range(num_spins):
        rho_i = rho.ptrace(i)
        purity_i = np.real((rho_i * rho_i).tr())
        Q += 1 - purity_i
    return 2 * Q / num_spins