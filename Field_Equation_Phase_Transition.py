import numpy as np
import matplotlib.pyplot as plt

def plot_phase_transition():
    phi = np.linspace(0, 3, 500)
    phi_c = 1.0  # Critical Threshold
    
    # Curvature (k) as a sigmoidal function of drive (Phi)
    k = 1 / (1 + np.exp(-6 * (phi - phi_c)))
    
    plt.figure(figsize=(10, 6))
    plt.plot(phi, k, color='darkblue', linewidth=3, label='Manifold Curvature ($k$)')
    plt.axvline(x=phi_c, color='red', linestyle='--', label='Critical Threshold ($\Phi_c$)')
    
    # Shading the regimes
    plt.fill_between(phi, k, where=(phi < phi_c), color='red', alpha=0.1, label='Dissociative/Snap Regime')
    plt.fill_between(phi, k, where=(phi >= phi_c), color='green', alpha=0.1, label='Integrative/Waking Regime')
    
    plt.title("GIFT Field Equation: $\Phi \\to k$ Phase Transition", fontsize=16)
    plt.xlabel("Interoceptive Drive ($\Phi$)", fontsize=12)
    plt.ylabel("Phenomenal Curvature ($k$)", fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == "__main__":
    plot_phase_transition()
