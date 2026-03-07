import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

alpha=1.0; beta=0.5; gamma=1.0; eta=0.5; theta=1.0; eps=0.01; I=0.8
t_long = np.linspace(0, 3000, 50000)

def get_fp(Phi):
    def sys(s, t, Phi):
        x, y = s; x = max(x, 1e-9)
        D = 1 - y**2 + eps
        return [alpha*(Phi-x) - beta*theta/D,
                gamma*(I-y) - eta*theta/(x*D)*y*(1-y**2)]
    sol = odeint(sys, [2.5, 0.7], t_long, args=(Phi,), rtol=1e-11)
    return sol[-1, 0]  # return Phi_int* as HEP proxy

# Pre-morbid baseline
Phi_baseline = 2.0
HEP_baseline = get_fp(Phi_baseline)

# Phase 1: Onset — Phi_target drops due to chronic stress build-up
onset_Phi = np.linspace(Phi_baseline, 0.7, 30)
onset_HEP = [get_fp(p) for p in onset_Phi]

# Phase 2a: Restoration (returns Phi_target to baseline) — insufficient
restore_Phi = np.linspace(0.7, Phi_baseline, 30)
restore_HEP = [get_fp(p) for p in restore_Phi]

# Phase 2b: Amplification (Phi_target raised above baseline) — sufficient
amplify_Phi = np.linspace(0.7, Phi_baseline + 0.8, 30)
amplify_HEP = [get_fp(p) for p in amplify_Phi]

fig, ax = plt.subplots(figsize=(11, 6))

# Onset trajectory
ax.plot(range(30), onset_HEP, 'b-o', ms=4, lw=2, label='Onset (Φ_target decreasing)')
# Restoration — joins from end of onset
ax.plot(range(29, 59), restore_HEP, 'orange', lw=2, ls='--', marker='s', ms=4,
        label='Restoration to baseline (insufficient)')
# Amplification
ax.plot(range(29, 59), amplify_HEP, 'g-^', ms=4, lw=2,
        label='Amplification above baseline (recovery)')

ax.axhline(HEP_baseline, color='k', ls='-.', lw=1.5, alpha=0.7,
           label=f'Pre-morbid HEP baseline ({HEP_baseline:.3f})')
ax.axhline(amplify_HEP[-1], color='green', ls=':', lw=1.5, alpha=0.7,
           label=f'Post-recovery HEP ({amplify_HEP[-1]:.3f}, exceeds baseline)')

ax.set_xlabel('Treatment Timepoint (arbitrary)', fontsize=12)
ax.set_ylabel('Predicted HEP Amplitude (Φᵢₙₜ* proxy)', fontsize=12)
ax.set_title('Figure E: Recovery Asymmetry Test Prediction\n'
             'HEP at remission must EXCEED pre-morbid baseline', fontsize=13)
ax.axvspan(0, 29, alpha=0.05, color='red', label='DPDR episode')
ax.axvspan(29, 59, alpha=0.05, color='green', label='Intervention phase')
ax.legend(fontsize=9, loc='lower right')
ax.grid(True, alpha=0.3)

# Annotate the gap
gap = amplify_HEP[-1] - restore_HEP[-1]
ax.annotate(f'Amplification gap\n(Δ = {gap:.3f})',
            xy=(58, (amplify_HEP[-1] + restore_HEP[-1])/2),
            xytext=(45, (amplify_HEP[-1] + restore_HEP[-1])/2 + 0.05),
            arrowprops=dict(arrowstyle='->', color='darkgreen'),
            fontsize=10, color='darkgreen')

plt.tight_layout()
plt.savefig('FigureE_HEP_recovery_prediction.png', dpi=150, bbox_inches='tight')
plt.show()
