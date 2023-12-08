# %% Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Technology constants
from constants import C_GS_per_W, C_DB_per_W, C_GD_per_W

# %% Constants
f_0 = 60e9 # Hz
omega_0 = 2 * np.pi * f_0 # rad / s
Vdd = 1.2 # V

# %% Port Matching Specs
R_RF = 50 # Ohm
R_BB = 50 # Ohm

# %% Decap sizing
R_b = R_RF * 20
C_decap = R_b / omega_0 * 20
print(f"{R_b = }")
print(f"{C_decap * 1e9 = }")


# %% Design transistor M1
ID1 = 2e-3 # A
gm_over_ID1 = 5 # Copy of 1/V
ID_over_W1 = 205 # A / m # Compute using cadence
VGS_min_VT1 = 610e-3 # V # Compute using cadence
gm1 = gm_over_ID1 * ID1 # Sm
W_M1 = ID1 / ID_over_W1
print(f"{gm1 = }")
print(f"{W_M1 * 1e6 = }")

C_GS_M1 = C_GS_per_W * W_M1 # F
C_GD_M1 = C_GD_per_W * W_M1 # F
C_DB_M1 = C_DB_per_W * W_M1 # F
print(f"{C_GS_M1 =  :.6e}")
print(f"{C_GD_M1 =  :.6e}")
print(f"{C_DB_M1 =  :.6e}")

L1_eq = 1 / (omega_0**2 * C_GS_M1) # H
print(f"{L1_eq * 1e12 = }")

L2 = R_RF * C_GS_M1 / gm1 # H
print(f"{L2 * 1e12 = }")

# %% Ideal results
A_ideal = gm1 * 100 * 2 / np.pi
A_ideal_dB = 20 * np.log10(A_ideal) 
print(f"{A_ideal_dB = }")

# %% Design transistor M2 & M2p
ID2 = ID1 / 2 / 2 # 1
gm_over_ID2 = 12 # Sm
gm2 = gm_over_ID2 * ID2 # Sm
ID_over_W2 = 45 # A / m # Compute using cadence
VGS_min_VT2 = 400e-3 # V # Compute using cadence
W_M2 = ID2 / ID_over_W2 # m
print(f"{gm2 = }")
print(f"{W_M2 * 1e6 = }")

C_GS_M2 = C_GS_per_W * W_M2 # F
C_GD_M2 = C_GD_per_W * W_M2 # F
C_DB_M2 = C_DB_per_W * W_M2 # F
print(f"{C_GS_M2 =  :.6e}")
print(f"{C_GD_M2 =  :.6e}")
print(f"{C_DB_M2 =  :.6e}")

# %% Design output resistors
R_out_max = (Vdd - 0.8) / ID2
print(f"{R_out_max = }")

# %% Design transistor M3 & M3p
gm3 = 1 / R_BB
gm_over_ID3 = 10
ID3 = gm3 / gm_over_ID3
print(f"{ID3 = }")

VGS_min_VT3 = 450e-3 # Get from Cadence
ID_over_W3 = 72 # Get from Cadence
W3 = ID3 / ID_over_W3 
print(f"{W3 * 1e6 = }")

# %% Desig current source M4 & M4p
gm_over_ID4 = 10
ID4 = ID3
gm4 = gm_over_ID4 * ID4
print(f"{gm4 = }")

ID_over_W4 = 72 # Get from Cadence
W4 = ID4 / ID_over_W4
print(f"{W4 * 1e6 = }")

# %% 1. Fix input impedance to 50 ohms by first tuning L2 for real part & then picking L1 for imaginary part

# %% 2. Tune L0 to Fight M0 drain capacitance
C_GG_M1 = 11.91e-15
C_DD_M1 = 3.245e-15
C_SS_M1 = 8.414e-15

C_GG_M2 = 12.43e-15
C_DD_M2 = 3.448e-15
C_SS_M2 = 8.473e-15

C_p0 = C_DD_M1 + 2 * C_SS_M2
L0 = 1 / (omega_0**2 * C_p0)
print(f"{L0 * 1e12 = }")

# %%
L5 = 220 / omega_0 / 2
print(f"{L5 = }")

# %%
C = 1e-14
print(f"{1 / (omega_0 * C) = }")
print(f"{1 / (2 * np.pi * 1e9 * C) = }")

# %%
