import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Define the H and S dimensions (The T_mu_nu components)
H = np.linspace(0.1, 1.0, 50) # Hierarchical Depth
S = np.linspace(0.1, 1.0, 50) # Counterfactual Horizon
H_grid, S_grid = np.meshgrid(H, S)

# Calculate Curvature G (Inference Cost/Variational Free Energy)
# In GIFT, G is inversely proportional to the integration of H and S
G_curvature = 1.0 / (H_grid * S_grid + 0.1)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(H_grid, S_grid, G_curvature, cmap=cm.magma, 
                       antialiased=True, alpha=0.8)

ax.set_title("GIFT Curvature: The Topological Cost of Presence", fontweight='bold')
ax.set_xlabel('Hierarchical Depth (H)')
ax.set_ylabel('Counterfactual Horizon (S)')
ax.set_zlabel('Belief Space Curvature (G)')

# Annotate the Snap
ax.text(0.1, 0.1, 10, "The Dissociative Snap", color='white', fontweight='bold')
fig.colorbar(surf, shrink=0.5, aspect=10, label='Metric Strain')
plt.show()
