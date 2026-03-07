import numpy as np
import matplotlib.pyplot as plt

# GIFT Parameters (HRIT Density Constants)
alpha, beta = 0.5, 0.8  # Homeostatic restoration vs Stress sensitivity
gamma, eta = 0.4, 0.6   # Coupling rate vs Recursive gain
phi_target, rho_target = 1.0, 0.8
F_stress = 0.6 # Moderate stress simulation

# Create Grid
phi_vals = np.linspace(0.1, 1.2, 20)
rho_vals = np.linspace(0.1, 0.95, 20)
PH, RH = np.meshgrid(phi_vals, rho_vals)

# Derivatives (GIFT ODE System)
dPhi = alpha * (phi_target - PH) - beta * F_stress * PH
dRho = gamma * (rho_target - RH) - eta * F_stress * RH * (1 - RH**2)

plt.figure(figsize=(10, 7), dpi=100)
# Removed 'alpha' to fix TypeError; using linewidth to indicate flow speed
magnitude = np.sqrt(dPhi**2 + dRho**2)
strm = plt.streamplot(PH, RH, dPhi, dRho, color=magnitude, cmap='viridis', linewidth=1.5*magnitude/magnitude.max())

# Add the 'Equilibrium Point' (The Waking Attractor)
plt.plot(0.52, 0.72, 'ro', markersize=10, label='Meta-Stable Self (Waking)')

plt.title("GIFT Stability Map: Attractor Dynamics under Stress", fontweight='bold')
plt.xlabel(r"Interoceptive Precision ($\Phi$)")
plt.ylabel(r"Autonoetic Coupling ($\rho$)")
plt.colorbar(strm.lines, label='Flow Magnitude')
plt.legend()
plt.grid(alpha=0.2)
plt.show()
