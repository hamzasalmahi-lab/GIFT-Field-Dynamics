import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

alpha=1.0; beta=0.5; gamma=1.0; eta=0.5; theta=1.0; eps=0.01; I=0.8
t = np.linspace(0, 3000, 50000)

def sys(s, t, Phi):
    x, y = s; x = max(x, 1e-9)
    D = 1 - y**2 + eps
    return [alpha*(Phi - x) - beta*theta/D,
            gamma*(I - y) - eta*theta/(x*D)*y*(1 - y**2)]

Phi_vals = np.linspace(3.0, 0.5, 60)
Psi_vals, xf_vals, yf_vals = [], [], []

for Phi in Phi_vals:
    sol = odeint(sys, [2.5, 0.7], t, args=(Phi,), rtol=1e-11)
    xf, yf = sol[-1]
    Psi = np.log(max(xf, 1e-9)) + np.log(max(1 - yf**2, 1e-9))
    Psi_vals.append(Psi); xf_vals.append(xf); yf_vals.append(yf)

fig, axes = plt.subplots(1, 3, figsize=(14, 4))

axes[0].plot(Phi_vals, Psi_vals, 'b-', lw=2)
axes[0].set_xlabel('Homeostatic Drive (Φ_target)', fontsize=12)
axes[0].set_ylabel('Conscious Intensity (Ψ)', fontsize=12)
axes[0].set_title('Ψ along the Fixed-Point Curve', fontsize=13)
axes[0].axhline(y=min(Psi_vals)*0.95, color='k', ls=':', alpha=0.3)
axes[0].grid(True, alpha=0.3)

axes[1].plot(Phi_vals, xf_vals, 'g-', lw=2, label='Φᵢₙₜ*')
axes[1].plot(Phi_vals, yf_vals, 'r-', lw=2, label='ρ*')
axes[1].set_xlabel('Homeostatic Drive (Φ_target)', fontsize=12)
axes[1].set_ylabel('Fixed-Point Coordinates', fontsize=12)
axes[1].set_title('Fixed Point vs Drive', fontsize=13)
axes[1].legend(); axes[1].grid(True, alpha=0.3)

axes[2].plot(xf_vals, yf_vals, 'purple', lw=2)
axes[2].set_xlabel('Φᵢₙₜ* (Self-Precision)', fontsize=12)
axes[2].set_ylabel('ρ* (Autonoetic Coupling)', fontsize=12)
axes[2].set_title('Fixed-Point Manifold in State Space', fontsize=13)
# Mark waking and dissociated ends
axes[2].plot(xf_vals[0], yf_vals[0], 'go', ms=10, label='High Φ (waking)')
axes[2].plot(xf_vals[-1], yf_vals[-1], 'rs', ms=10, label='Low Φ (dissociated)')
axes[2].legend(); axes[2].grid(True, alpha=0.3)

plt.suptitle('Figure A: GIFT Fixed-Point Curve and Conscious Intensity', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('FigureA_fixed_point_curve.png', dpi=150, bbox_inches='tight')
plt.show()
print("Done.")
