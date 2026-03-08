# GIFT-Field-Dynamics

This repository contains the formal mathematical simulations for **Generative Inferential Frame Theory (GIFT)**. While HRIT describes the neurobiological architecture of consciousness, GIFT provides the underlying physicalist engine—modeling consciousness as the **topology of the belief manifold**.

##  Theoretical Core
GIFT proposes that phenomenal presence is a function of the curvature ($k$) of an inferential field, driven by interoceptive-affective precision ($\Phi$). 

### Key Constructs:
* **Interoceptive Drive ($\Phi$):** The gain/precision of the homeostatic generative model.
* **Belief Manifold:** The multidimensional state space of the agent's generative model.
* **The Phenomenal Snap:** A phase transition where the manifold flattens as $\Phi$ drops below a critical threshold ($\Phi_c$), resulting in the "unreal" quality of dissociation.

## Included Simulations

### 1. Theoretical Topology (The Geometry of Presence)

**Focus:** Formalizing the relationship between the field equation  
`G_{μν} = κT_{μν}`

- **Manifold_Deformation_3D.py**  
  High-fidelity visualization of the belief manifold's *predictive grip* as a function of precision-weighting.

- **The_Curvature_of_Presence.py**  
  Explores the interaction between **Hierarchical Depth (H)** and **Self-Representation (S)** variables.

- **Eigenvalue_Structure_Along_the_Fixed_Point_Curve.py**  
  Establishes the mathematical stability and **monostability** of the **GIFT global attractor**.


### 2. Nonlinear Dynamics & Phase Transitions

**Focus:** Modeling the *Phenomenal Snap* and pathological persistence.

- **Field_Equation_Phase_Transition.py**  
  Core simulation engine modeling the transition from **Waking Presence** to **Dissociative Flattening**.

- **Hysteresis_Loop.py**  
  Simulates the **recovery lag** observed in clinical states, demonstrating why the onset of dissociation is not symmetrical with recovery.

- **Fixed_Stability_Map_Phase_Portrait.py**  
  Vector-field analysis of the system’s attractor states across the `Φ` gradient.


### 3. Clinical Translation & Biomarker Prediction

**Focus:** Bridging theory with clinical application.

- **Critical_Slowing_Down_Biomarker_Prediction.py**  
  Implements dynamical systems indicators to predict impending **conscious collapse**.

- **HEP_Amplitude_Prediction.py**  
  Models the relationship between **manifold depth** and **Heart-Evoked Potentials (HEP)**.

- **Recovery_Time_Predictor.py**  
  Prognostic simulation estimating **clinical recovery windows** based on interoceptive gain restoration.
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
