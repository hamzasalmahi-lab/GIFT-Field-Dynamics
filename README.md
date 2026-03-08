# GIFT-Field-Dynamics

This repository contains the formal mathematical simulations for **Generative Inferential Frame Theory (GIFT)**. While HRIT describes the neurobiological architecture of consciousness, GIFT provides the underlying physicalist engine—modeling consciousness as the **topology of the belief manifold**.

##  Theoretical Core
GIFT proposes that phenomenal presence is a function of the curvature ($k$) of an inferential field, driven by interoceptive-affective precision ($\Phi$). 

### Key Constructs:
* **Interoceptive Drive ($\Phi$):** The gain/precision of the homeostatic generative model.
* **Belief Manifold:** The multidimensional state space of the agent's generative model.
* **The Phenomenal Snap:** A phase transition where the manifold flattens as $\Phi$ drops below a critical threshold ($\Phi_c$), resulting in the "unreal" quality of dissociation.

##  Included Simulations

### 1. Theoretical Topology (The Geometry of Presence)
Focus: Formalizing the $G_{\mu\nu} = \kappa T_{\mu\nu}$ relationship.
    Manifold_Deformation_3D.py: A high-fidelity visualization of the belief manifold's "predictive grip" as a function of precision-      weighting.
    The Curvature of Presence.py: Explores the interaction between Hierarchical depth (H) and Self-representation (S) variables.
    Eigenvalue_structure_along_the_fixed-point_curve.py: Establishes the mathematical stability and monostability of the GIFT global      attractor.


### 2. Nonlinear Dynamics & Phase Transitions
Focus: Modeling the "Phenomenal Snap" and Pathological Persistence.
    Field_Equation_Phase_Transition.py: The primary engine for simulating the transition from Waking Presence to Dissociative  Flattening.
    The Hysteresis Loop.py: Models the "recovery lag" in clinical states, demonstrating why the onset of dissociation is non-symmetrical with recovery.
    Fixed Stability Map (Phase Portrait).py: Vector field analysis of the system's attractor states across the $\Phi$ gradient.
    

### 3. Clinical Translation & Biomarker Prediction
Focus: Moving from theory to the hospital bedside.
    Critical Slowing Down (Biomarker Prediction).py: Implementation of dynamical systems indicators to predict impending "Conscious Collapse."
    HEP amplitude prediction.py: Models the correlation between manifold depth and Heart-Evoked Potentials (HEP).
    The Recovery Time Predictor.py: A prognostic script for estimating clinical recovery windows based on interoceptive gain recovery.

##  Technical Implementation
Mathematical Basis
The simulations are grounded in:

Active Inference (Variational Free Energy Minimization)

Riemannian Geometry of statistical manifolds

Non-linear Dynamical Systems (ODE solvers)

##  Usage
These scripts require Python 3.x and the standard scientific stack:
```bash
pip install numpy matplotlib scipy networkx

##  Academic Correspondence
Hamza S. Almahi, MBBS Strategy & Research | Theoretical Neuroscience 
Email: hamza.s.almahi@gmail.com

LinkedIn: (https://www.linkedin.com/in/hamza-almahi-2a09a3127/)
