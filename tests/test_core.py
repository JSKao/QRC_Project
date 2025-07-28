import numpy as np
from qutip import basis, tensor
from qrc.core.hamiltonian import TFIMHamiltonian
from qrc.core.evolution import QRCEvolution
from qrc.core.measurement import QuantumMeasurement

def test_hamiltonian_build():
    h = TFIMHamiltonian(num_spins=3, h=1, Js=1, seed=42)
    H = h.build()
    assert H.shape[0] == 8  # 2^3
    assert H.shape[1] == 8
    
def test_inject_input_shape():
    num_spins = 3
    evo = QRCEvolution(num_spins=num_spins)
    psi = tensor([basis(2, 0) for _ in range(num_spins)])
    rho = psi * psi.dag()
    rho_new = evo.inject_input(rho, 0.5)
    assert rho_new.shape[0] == 8
    assert rho_new.shape[1] == 8    
    
def test_measure_all():
    num_spins = 3
    meas = QuantumMeasurement(num_spins=num_spins)
    psi = tensor([basis(2, 0) for _ in range(num_spins)])
    rho = psi * psi.dag()
    results = meas.measure_all(rho)
    assert len(results) == num_spins
    # |000> 慣常下 <sz> = 1
    assert all(abs(x - 1.0) < 1e-8 for x in results)    