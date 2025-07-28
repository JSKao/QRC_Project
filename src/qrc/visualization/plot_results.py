# filepath: src/qrc/visualization/plot_results.py
import matplotlib.pyplot as plt

def plot_observables(tlist, expectation_values, num_spins):
    plt.figure(figsize=(10, 4))
    for j in range(num_spins):
        plt.plot(tlist, expectation_values[j], label=f'Spin{j+1}')
    plt.xlim([0, min(100, len(tlist))])
    plt.ylim([-1, 1])
    plt.xlabel('Time')
    plt.ylabel(r'$\langle \sigma_z \rangle$')
    plt.title('Time Evolution of Spin Network under transverse-field')
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_distance(tlist, distance_values, delta_t):
    plt.figure(figsize=(10, 4))
    for j, dist in enumerate(distance_values):
        plt.plot(tlist, dist, label=f'Δt = {delta_t[j]}')
    plt.xlim([0, min(300, len(tlist))])
    plt.xlabel('Time')
    plt.ylabel(r'$||\rho_A - \rho_B||$')
    plt.title('Time evolved convergence of two distant initial states')
    plt.legend()
    plt.tight_layout()
    plt.show()