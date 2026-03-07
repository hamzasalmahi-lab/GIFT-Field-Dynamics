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

def jacobian(xf, yf):
    D = 1 - yf**2 + eps
    return np.array([
        [-alpha, -2*beta*theta*yf/D**2],
        [eta*theta*yf/xf**2, -eta*theta/xf - gamma]
    ])

Phi_vals = np.linspace(3.0, 0.6, 60)
lam1_vals, lam2_vals, det_vals, tr_vals = [], [], [], []

for Phi in Phi_vals:
    sol = odeint(sys, [2.5, 0.7], t, args=(Phi,), rtol=1e-11)
    xf, yf = sol[-1]
    J = jacobian(xf, yf)
    eigs = sorted(np.linalg.eigvals(J).real)
    lam1_vals.append(eigs[0]); lam2_vals.append(eigs[1])
    det_vals.append(np.linalg.det(J)); tr_vals.append(np.trace(J))

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].plot(Phi_vals, lam1_vals, 'b-', lw=2, label='λ₁ (more negative)')
axes[0].plot(Phi_vals, lam2_vals, 'r-', lw=2, label='λ₂ (less negative)')
axes[0].axhline(0, color='k', ls='--', lw=1, alpha=0.5)
axes[0].fill_between(Phi_vals, lam1_vals, 0, alpha=0.1, color='blue')
axes[0].set_xlabel('Homeostatic Drive (Φ_target)', fontsize=12)
axes[0].set_ylabel('Eigenvalue (real part)', fontsize=12)
axes[0].set_title('Eigenvalues: System Stiffens as Drive Decreases', fontsize=13)
axes[0].legend(); axes[0].grid(True, alpha=0.3)
axes[0].annotate('Both eigenvalues become\nmore negative → system\nstiffens, does NOT slow',
                 xy=(0.8, lam1_vals[-5]), xytext=(1.5, -4),
                 arrowprops=dict(arrowstyle='->', color='black'),
                 fontsize=10, color='darkblue')

axes[1].plot(Phi_vals, det_vals, 'g-', lw=2, label='det(J)')
ax2 = axes[1].twinx()
ax2.plot(Phi_vals, tr_vals, 'orange', lw=2, ls='--', label='tr(J)')
axes[1].set_xlabel('Homeostatic Drive (Φ_target)', fontsize=12)
axes[1].set_ylabel('det(J)', color='g', fontsize=12)
ax2.set_ylabel('tr(J)', color='orange', fontsize=12)
axes[1].set_title('Jacobian Invariants: det(J) > 0, tr(J) < 0 Throughout', fontsize=13)
axes[1].axhline(0, color='k', ls='--', lw=1, alpha=0.5)
axes[1].grid(True, alpha=0.3)
lines1, labels1 = axes[1].get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
axes[1].legend(lines1+lines2, labels1+labels2)

plt.suptitle('Figure B: Eigenvalue Structure — No Critical Slowing Down', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('FigureB_eigenvalues.png', dpi=150, bbox_inches='tight')
plt.show()
