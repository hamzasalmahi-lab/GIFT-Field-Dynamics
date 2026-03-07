import numpy as np
import matplotlib.pyplot as plt

def solve_equilibrium(phi_drive):
    """ Simplified GIFT equilibrium for the self-state 'u' """
    # u^3 - u + phi = 0 (Standard Cusp Catastrophe form)
    # We solve for the roots of the potential
    roots = np.roots([1, 0, -1, phi_drive])
    real_roots = roots[np.isreal(roots)].real
    return real_roots

# Stress path: High to Low and Low to High
stress_increasing = np.linspace(-0.6, 0.6, 100)
stress_decreasing = stress_increasing[::-1]

plt.figure(figsize=(9, 6))

# Forward Path
u_fwd = [max(solve_equilibrium(s)) for s in stress_increasing]
plt.plot(stress_increasing, u_fwd, 'b', label='Stress Increasing (Path to Snap)')

# Backward Path
u_bwd = [min(solve_equilibrium(s)) for s in stress_decreasing]
plt.plot(stress_decreasing, u_bwd, 'r--', label='Stress Decreasing (Path to Recovery)')

plt.annotate('The Dissociative Snap', xy=(0.38, 0.6), xytext=(0.45, 1.2),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('Hysteresis Gap\n(Chronic DPDR)', xy=(-0.1, -0.2), fontweight='bold')

plt.title("GIFT Hysteresis: The Irreversibility of the Self-Model Collapse", fontweight='bold')
plt.xlabel("Free Energy Stress (Environmental Noise)")
plt.ylabel("Recursive Integration Strength (u)")
plt.legend()
plt.grid(alpha=0.2)
plt.show()
