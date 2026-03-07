import numpy as np
import matplotlib.pyplot as plt

def impulse_response(stability_lambda, t):
    return np.exp(stability_lambda * t)

t = np.linspace(0, 10, 100)
stabilities = [-2.0, -1.0, -0.2] # High stability to Criticality
labels = ['Stable Waking', 'Resonance Ridge', 'Near-Snap']
colors = ['green', 'orange', 'red']

plt.figure(figsize=(10, 5))
for lam, label, color in zip(stabilities, labels, colors):
    plt.plot(t, impulse_response(lam, t), label=label, color=color, linewidth=2)

plt.axhline(y=0.1, color='gray', linestyle='--', label='Recovery Threshold')
plt.title("Critical Slowing Down: Recovery Latency as a Diagnostic", fontweight='bold')
plt.xlabel("Time (ms)")
plt.ylabel("Presence Displacement ($\Delta G$)")
plt.legend()
plt.show()
