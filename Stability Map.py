import numpy as np
import matplotlib.pyplot as plt

# GIFT Parameters (Fixed for visibility)
alpha, beta = 0.5, 0.8
gamma, eta = 0.4, 0.6
phi_target, rho_target = 1.0, 0.8
F_stress = 0.5 # High stress environment

# Grid
phi_vals = np.linspace(0.1, 1.2, 20)
rho_vals = np.linspace(0.1, 0.95, 20)
PH, RH = np.meshgrid(phi_vals, rho_vals)

# Derivatives
dPhi = alpha * (phi_target - PH) - beta * F_stress * PH
dRho = gamma * (rho_target - RH) - eta * F_stress * RH * (1 - RH**2)

plt.figure(figsize=(10, 8), dpi=100)
# Fix: Removed alpha to avoid TypeError
strm = plt.streamplot(PH, RH, dPhi, dRho, color=np.sqrt(dPhi**2 + dRho**2), 
                      cmap='autumn', linewidth=1.5)

# Add Nullclines (Where the system stops moving)
# alpha(phi_t - phi) - beta*F*phi = 0  => phi = (alpha*phi_t) / (alpha + beta*F)
phi_null = (alpha * phi_target) / (alpha + beta * F_stress)
plt.axvline(x=phi_null, color='blue', linestyle='--', label=r'$\dot{\Phi}=0$ Nullcline')

plt.title("GIFT Stability Map: Attractor Dynamics under Stress", fontweight='bold')
plt.xlabel(r"Interoceptive Precision ($\Phi$)")
plt.ylabel(r"Autonoetic Coupling ($\rho$)")
plt.colorbar(strm.lines, label='Flow Velocity')
plt.legend()
plt.show()
