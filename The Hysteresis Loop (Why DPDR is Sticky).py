import numpy as np
import matplotlib.pyplot as plt

def solve_equilibrium(stress):
    """ Simplified GIFT potential roots """
    # u^3 - u + stress = 0
    roots = np.roots([1, 0, -1, stress])
    real_roots = roots[np.isreal(roots)].real
    return real_roots

stress_range = np.linspace(-0.6, 0.6, 150)
stress_fwd = stress_range
stress_bwd = stress_range[::-1]

plt.figure(figsize=(9, 6))

# Forward path (Into the snap)
u_fwd = [max(solve_equilibrium(s)) for s in stress_fwd]
plt.plot(stress_fwd, u_fwd, 'b', label='Stress Increasing (Healthy to Snap)')

# Backward path (Recovery)
u_bwd = [min(solve_equilibrium(s)) for s in stress_bwd]
plt.plot(stress_bwd, u_bwd, 'r--', label='Stress Decreasing (Recovery Pathway)')

plt.title("Hysteresis in GIFT: Topological Memory of Trauma", fontweight='bold')
plt.xlabel("Stress Density ($T_{stress}$)")
plt.ylabel("Recursive Presence ($R$)")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
