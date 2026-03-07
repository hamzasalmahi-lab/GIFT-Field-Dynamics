import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def simulate_manifold():
    x = np.linspace(-2, 2, 100)
    y = np.linspace(-2, 2, 100)
    X, Y = np.meshgrid(x, y)
    
    # Define three Phi states: Waking (2.0), Critical (1.0), Snap (0.2)
    phi_states = [2.0, 1.0, 0.2]
    labels = ['Waking Presence ($\Phi > \Phi_c$)', 'Critical Threshold ($\Phi \\approx \Phi_c$)', 'Phenomenal Snap ($\Phi < \Phi_c$)']
    colors = ['viridis', 'plasma', 'magma']

    fig = plt.figure(figsize=(18, 6))

    for i, phi in enumerate(phi_states):
        ax = fig.add_subplot(1, 3, i+1, projection='3d')
        # GIFT Manifold Equation: Z represents energy depth
        Z = phi * (X**2 + Y**2) * np.exp(-0.5 * (X**2 + Y**2))
        
        surf = ax.plot_surface(X, Y, Z, cmap=colors[i], edgecolor='none', alpha=0.9)
        ax.set_title(labels[i], fontsize=14)
        ax.set_zlim(0, 1.5)
        ax.view_init(elev=25, azim=45)
        ax.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    simulate_manifold()
