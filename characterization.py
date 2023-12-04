# %% Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# %% Load result
results_dir = "./results"
nmos_y_params_path = os.path.join(results_dir, "nmos_y_params.csv")
nmos_y_params_df = pd.read_csv(nmos_y_params_path)

# %%
nmos_y_params_df.head()



# %%

f = nmos_y_params_df["Y11 imS X"]
omega = 2 * np.pi * f
Y11 = nmos_y_params_df["Y11 reS Y"] + 1j * nmos_y_params_df["Y11 imS Y"]
Y21 = nmos_y_params_df["Y21 reS Y"] + 1j * nmos_y_params_df["Y21 imS Y"]
Y12 = nmos_y_params_df["Y12 reS Y"] + 1j * nmos_y_params_df["Y12 imS Y"]
Y22 = nmos_y_params_df["Y22 reS Y"] + 1j * nmos_y_params_df["Y22 imS Y"]


fig, ax = plt.subplots()
ax.plot(f, np.abs(Y11), label="Y11")
ax.plot(f, np.abs(Y21), label="Y21")
ax.plot(f, np.abs(Y12), label="Y12")
ax.plot(f, np.abs(Y22), label="Y22")
ax.legend()
#ax.set_xscale("log")

# %% Extract parameters
mask = (f >= 10e9) * (f <= 100e9)
i = np.argmin(np.abs(f - 60e9))

rg = np.real(1 / Y11)
fig, ax = plt.subplots()
ax.plot(f[mask], rg[mask])
ax.set_title("rg")
print(f"{rg[i] = }")

gm = np.real(Y21)
fig, ax = plt.subplots()
ax.plot(f[mask], gm[mask])
ax.set_title("gm")
print(f"{gm[i] = }")

r0 = 1/np.real(Y22)
fig, ax = plt.subplots()
ax.plot(f[mask], r0[mask])
ax.set_title("r0")
print(f"{r0[i] = }")


Cgs = (-1 / np.imag(1 / Y11) + np.imag(Y12)) / omega
fig, ax = plt.subplots()
ax.plot(f[mask], Cgs[mask])
ax.set_title("Cgs")
print(f"{Cgs[i] = :.6e}")

Cgd = - np.imag(Y12) / omega
fig, ax = plt.subplots()
ax.plot(f[mask], Cgd[mask])
ax.set_title("Cgd")
print(f"{Cgd[i] = :.6e}")

Cdb = np.imag(Y22) / omega - Cgd
fig, ax = plt.subplots()
ax.plot(f[mask], Cgd[mask])
ax.set_title("Cgd")
print(f"{Cdb[i] = :.6e}")


# %% Design constants
L = 100e-9
W = 1e-6
W_over_L = W/L
ID = 616.7e-6
gm_over_ID = gm[i] / ID


# %% Technology Constants

print(f"{Cgs[i] / W}")
print(f"{Cgd[i] / W}")
print(f"{Cdb[i] / W}")

# %%
