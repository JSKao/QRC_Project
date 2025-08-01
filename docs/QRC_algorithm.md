# Quantum Reservoir Computing (QRC) Algorithm Overview

**Generic Quantum System (Take Transverse Field Ising model as example)**

$H = \sum_{i < j} J_{ij} \sigma_x^{(i)} \sigma_x^{(j)} + h \sum_{i} \sigma_z^{(i)} $

- $J_{ij}$: Random coupling strength, sampled uniformly from $[-J_s/2, J_s/2]$.
- $h$: Transverse field strength.
- $\sigma_x^{(i)}$, $\sigma_z^{(i)}$: Pauli matrices for the $i$-th spin.

### QRC Simulation Steps

1. **Time Evolution**  
   Compute the time evolution operator using the Hamiltonian: 

   $U(t) = e^{-i H t}$

   The quantum state evolves as:  

   $\rho(t + \Delta t) = U(\Delta t) \rho(t) U^\dagger(\Delta t)$

2. **Input Injection**  
   At each time interval $\Delta t$, encode a random input $s \in [0, 1]$ as a quantum state:  
   $\psi_{\text{inject}}\rangle = \sqrt{1-s} |0\rangle + \sqrt{s} \rangle $
   The new system state is updated by tensoring the injected state with the reduced system:  
   $\rho_{\text{new}} = |\psi_{\text{inject}}\rangle\langle\psi_{\text{inject}}| \otimes \rho_{\text{reduced}}$

3. **Measurement**  
   For each spin, compute the expectation value (e.g., for $\sigma_z$):  
   $\langle \sigma_z^{(i)} \rangle = \text{Tr}(\rho \cdot \sigma_z^{(i)})$

4. **State Distance**  
   Quantify the difference between two quantum states using the Hilbert-Schmidt distance:  
   $D(\rho_1, \rho_2) = \sqrt{\text{Tr}[(\rho_1 - \rho_2)^2]}$

---

# QRC Analysis Tools

## 1. Short-Term Memory (STM)

STM quantifies the system's ability to remember past inputs. It is based on the correlation between the input sequence and the system's output.

**Formula:**  
$MC = \sum_{\tau} \text{Corr}^2(y(t), x(t-\tau))$
Where:
- $x(t)$: Input sequence
- $y(t)$: System output
- $\tau$: Time delay
- $\text{Corr}$: Correlation coefficient

**Typical Steps:**
1. Generate a random input sequence $x(t)$.
2. Simulate the system response $y(t)$.
3. Compute the correlation between $x(t-\tau)$ and $y(t)$ for various $\tau$.

---

## 2. Quantum Information Capacity

### a. Entanglement Entropy

Analyze the quantum state's entanglement by computing the von Neumann entropy of the reduced density matrix:
$S(\rho) = -\text{Tr}(\rho \log_2 \rho)$
where $\rho$ is the reduced density matrix after tracing out part of the system.

### b. Quantum Channel Simulation

Simulate the effect of a quantum channel (e.g., depolarizing channel) on the quantum state:
$\mathcal{E}(\rho) = (1-p) \rho + p \frac{\mathbb{I}}{d}$
where $p$ is the noise strength and $d$ is the Hilbert space dimension.

### c. Quantum Measurement Simulation

Simulate projective measurement on the quantum state:
$P_k = |\psi_k\rangle \langle \psi_k|, \quad \rho_{\text{post}} = \frac{P_k \rho P_k}{\text{Tr}(P_k \rho)}$
where $P_k$ is the measurement operator and $\rho_{\text{post}}$ is the post-measurement state.

---

## 3. Memory Capacity (MC)

Memory capacity quantifies how well the system can recall past inputs:
$MC = \sum_{\tau} \text{Corr}^2(y(t), x(t-\tau))$
where $\text{Corr}$ is the correlation between input $x(t-\tau)$ and output $y(t)$, and $\tau$ is the delay.

---

## 4. State Diversity

Analyze the diversity of system states by computing the entropy of the state distribution:
$H = -\sum_{i} p_i \log_2 p_i $
where $p_i$ is the probability of the $i$-th state.

---

## 5. Input-Output Mapping

Design input sequence $x(t)$ and output sequence $y(t)$, and learn the mapping:
$y(t) = f(x(t), x(t-1), \dots, x(t-\tau))$
where $f$ is determined by the quantum state evolution and measurement results.

---
