# %% Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Technology constants
from constants import C_GS_per_W, C_DB_per_W, C_GD_per_W

# %% Constants
f_0 = 60e9
omega_0 = 2 * np.pi * f_0

# %% RF Input port matching
R_RF = 50

# %% Design transistor M1
ID1 = 3e-3 # A
gm_over_ID1 = 10 # Copy of 1/V
ID_over_W1 = 72 # A / m # Compute using cadence
gm1 = gm_over_ID1 * ID1 # Sm
W_M1 = ID1 / ID_over_W1
print(f"{W_M1 * 1e6 = }")

C_GS_M1 = C_GS_per_W * W_M1 # F
C_GD_M1 = C_GD_per_W * W_M1 # F
C_DB_M1 = C_DB_per_W * W_M1 # F
print(f"{C_GS_M1 =  :.6e}")
print(f"{C_GD_M1 =  :.6e}")
print(f"{C_DB_M1 =  :.6e}")

L1_eq = 1 / (omega_0**2 ** C_GS_M1) # H
print(f"{L1_eq = }")

L2 = R_RF * C_GS_M1 / gm1 # H
print(f"{L2 = }")

# %% Design transistor M2 & M2p
ID2 = 1.5e-3 # 1
gm_over_ID2 = 10 # Sm
gm2 = gm_over_ID2 * ID2 # Sm
ID_over_W2 = 72 # A / m # Compute using cadence
W_M2 = ID2 / ID_over_W2 # m

print(f"{W_M2 * 1e6 = }")

C_GS_M2 = C_GS_per_W * W_M2 # F
C_GD_M2 = C_GD_per_W * W_M2 # F
C_DB_M2 = C_DB_per_W * W_M2 # F
print(f"{C_GS_M2 =  :.6e}")
print(f"{C_GD_M2 =  :.6e}")
print(f"{C_DB_M2 =  :.6e}")

# %% Combat parasitics
Cp1 = C_DB_M1
Cp2 = C_GS_M2 * 2
Cp3 = C_DB_M2


