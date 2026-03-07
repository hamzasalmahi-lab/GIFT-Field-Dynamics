import numpy as np
import matplotlib.pyplot as plt

def simulate_recovery(phi_level, perturbation=0.5):
    t = np.linspace(0, 20, 200)
    # Linearized recovery: u(t) = exp(lambda * t)
    # lambda = -2 * sqrt(phi) in our GIFT model
    lam = -2 * np.sqrt(max(0.01, phi_level))
    recovery = perturbation * np.exp(lam * t)
    return t, recovery

phi_levels = [1.5, 1.1, 1.01] # From stable to near-critical
colors = ['green', 'orange', 'red']

plt.figure(figsize=(9, 5))
for p, c in zip(phi_levels, colors):
    t, rec = simulate_recovery(p)
    plt.plot(t, rec, color=c, label=f'Drive $\Phi$ = {p}')

plt.title("Critical Slowing Down: Recovery Latency as a Biomarker", fontweight='bold')
plt.xlabel("Time after Perturbation (ms)")
plt.ylabel("State Displacement ($\Delta u$)")
plt.legend(title="Stability Level")
plt.axhline(y=0.05, color='gray', linestyle=':', label='Recovery Threshold')
plt.show()
