import numpy as np
import matplotlib.pyplot as plt

# Define the coordinates (Interoceptive Precision vs Autonoetic Coupling)
phi_int = np.linspace(0.01, 1.0, 100)
rho_sr = np.linspace(0.01, 0.99, 100)
P, R = np.meshgrid(phi_int, rho_sr)

# Fixed exteroceptive precision (sensory clarity)
pi_ext = 1.0 

# Calculate Psi (Conscious Intensity / Metric Volume)
# We use a small epsilon to avoid log(0)
Psi = np.log(pi_ext) + np.log(P) + np.log(1 - R**2 + 1e-5)

plt.figure(figsize=(10, 8))
cp = plt.contourf(P, R, Psi, levels=50, cmap='magma')
plt.colorbar(cp, label=r'Conscious Intensity ($\Psi$)')

# Add the 'Snap' Line
plt.axvline(x=0.2, color='white', linestyle='--', alpha=0.6)
plt.text(0.22, 0.5, "Metric Collapse Threshold", color='white', rotation=90)

plt.title("The Volume of the Belief Manifold (Metric Depth)", fontsize=14, fontweight='bold')
plt.xlabel(r"Interoceptive Grounding ($\Phi_{int}$)")
plt.ylabel(r"Self-Model Coupling ($\rho_{sr}$)")
plt.show()
