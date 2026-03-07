import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

alpha=1.0; beta=0.5; gamma=1.0; eta=0.5; theta=1.0; eps=0.01; I=0.8

def sys_triggered(s, t, Phi_base, trigger_start, trigger_end,
                  trigger_drop, recovery_start, recovery_boost):
    x, y = s; x = max(x, 1e-9)
    D = 1 - y**2 + eps
    # Phi_target varies with time
    if trigger_start <= t < trigger_end:
        Phi = Phi_base - trigger_drop        # Trigger drops drive
    elif t >= recovery_start:
        Phi = Phi_base + recovery_boost      # Recovery requires above-baseline
    else:
        Phi = Phi_base
    return [alpha*(Phi - x) - beta*theta/D,
            gamma*(I - y) - eta*theta/(x*D)*y*(1 - y**2)]

t = np.linspace(0, 800, 30000)
Phi_base = 2.0

# Scenario 1: Trigger only (no recovery boost) — stays depressed
sol1 = odeint(sys_triggered, [1.5, 0.6], t,
              args=(Phi_base, 50, 80, 1.6, 9999, 0.0), rtol=1e-10)

# Scenario 2: Trigger then restore to baseline — insufficient
sol2 = odeint(sys_triggered, [1.5, 0.6], t,
              args=(Phi_base, 50, 80, 1.6, 200, 0.0), rtol=1e-10)

# Scenario 3: Trigger then boost above baseline — recovery
sol3 = odeint(sys_triggered, [1.5, 0.6], t,
              args=(Phi_base, 50, 80, 1.6, 200, 0.8), rtol=1e-10)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# Φᵢₙₜ traces
ax1.plot(t, sol1[:,0], 'r-', lw=1.5, alpha=0.8, label='No intervention')
ax1.plot(t, sol2[:,0], 'orange', lw=1.5, label='Restored to baseline (insufficient)')
ax1.plot(t, sol3[:,0], 'g-', lw=2, label='Amplified above baseline (recovery)')
ax1.axvline(50, color='gray', ls=':', alpha=0.7, label='Trigger onset')
ax1.axvline(80, color='gray', ls='--', alpha=0.7, label='Trigger end')
ax1.axvline(200, color='blue', ls=':', alpha=0.7, label='Intervention start')
ax1.axhline(sol3[0,0], color='k', ls='-.', lw=1, alpha=0.5, label='Pre-morbid Φᵢₙₜ*')
ax1.set_ylabel('Interoceptive Precision (Φᵢₙₜ)', fontsize=12)
ax1.set_title('Recovery Asymmetry: Amplification Required, Not Restoration', fontsize=13)
ax1.legend(fontsize=9); ax1.grid(True, alpha=0.3)

# Ψ traces
for sol, color, label in [(sol1,'r','No intervention'),
                           (sol2,'orange','Restored to baseline'),
                           (sol3,'g','Amplified above baseline')]:
    Psi = np.log(np.maximum(sol[:,0], 1e-9)) + np.log(np.maximum(1 - sol[:,1]**2, 1e-9))
    ax2.plot(t, Psi, color=color, lw=1.5, label=label)
ax2.axvline(50, color='gray', ls=':', alpha=0.7)
ax2.axvline(80, color='gray', ls='--', alpha=0.7)
ax2.axvline(200, color='blue', ls=':', alpha=0.7)
ax2.set_xlabel('Time (AU)', fontsize=12)
ax2.set_ylabel('Conscious Intensity (Ψ)', fontsize=12)
ax2.set_title('Ψ During DPDR Episode and Recovery', fontsize=13)
ax2.legend(fontsize=9); ax2.grid(True, alpha=0.3)

plt.suptitle('Figure C: Recovery Asymmetry — F_self Drain Cycle', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('FigureC_recovery_asymmetry.png', dpi=150, bbox_inches='tight')
plt.show()
