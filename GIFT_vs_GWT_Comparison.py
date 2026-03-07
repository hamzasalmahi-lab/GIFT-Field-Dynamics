import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def compare_models():
    fig = plt.figure(figsize=(14, 6))

    # --- Subplot 1: GWT (Global Workspace Theory) ---
    # This represents consciousness as a discrete network broadcast
    ax1 = fig.add_subplot(1, 2, 1)
    G = nx.complete_graph(10) # 10 highly connected nodes
    pos = nx.spring_layout(G)
    nx.draw(G, pos, ax=ax1, node_color='skyblue', edge_color='gray', 
            node_size=600, with_labels=False, alpha=0.7)
    ax1.set_title("Global Workspace Theory (GWT)\nMechanism: Network Broadcast / Integration", fontsize=14)

    # --- Subplot 2: GIFT (Generative Inferential Frame Theory) ---
    # This represents consciousness as a continuous topological manifold
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    
    # Create the grid for the manifold
    u = np.linspace(-1.5, 1.5, 30)
    v = np.linspace(-1.5, 1.5, 30)
    U, V = np.meshgrid(u, v)
    
    # The GIFT Field Equation (Visualizing curvature 'k')
    # High curvature = High presence
    W = -(U**2 + V**2) 
    
    # Plot the surface (The Manifold)
    surf = ax2.plot_wireframe(U, V, W, color='purple', alpha=0.5)
    
    # Add the 'Operating Point' (The Red Dot from Figure 1)
    ax2.scatter([0], [0], [0], color='red', s=150, label='Phenomenal Center')
    
    ax2.set_title("GIFT\nMechanism: Field Topology / Curvature ($k$)", fontsize=14)
    ax2.set_zlim(-2, 1)
    ax2.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    compare_models()
