#Defuzzification


import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Universe of discourse
x = np.arange(0, 10.1, 0.1)

# --- 1. Max-Membership Principle (MoM) ---
mfx_trap = fuzz.trapmf(x, [3, 5, 7, 9])
mom_val = fuzz.defuzz(x, mfx_trap, 'mom')

# --- 2. Centroid Method ---
mfx_tri = fuzz.trimf(x, [2, 5, 8])
centroid_val = fuzz.defuzz(x, mfx_tri, 'centroid')

# --- 3. Weighted Average Method ---
centers = np.array([2, 5, 8])
weights = np.array([0.4, 0.8, 0.6])
wa_val = np.sum(centers * weights) / np.sum(weights)

# Print results
print("--- Defuzzification Results ---")
print(f"MoM: {mom_val:.2f}")
print(f"Centroid: {centroid_val:.2f}")
print(f"Weighted Average: {wa_val:.2f}")

# Plot setup
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle('Defuzzification Methods (MoM | Centroid | Weighted Avg)', fontsize=14)

# Plot 1: MoM
ax = axes[0]
ax.plot(x, mfx_trap, 'k', linewidth=2.5)
ax.axvline(mom_val, color='g', linestyle='--', label=f'MoM = {mom_val:.2f}')
ax.set_title('Mean of Maximum (MoM)')
ax.set_ylim(-0.05, 1.05)
ax.legend()
ax.grid(True)

# Plot 2: Centroid
ax = axes[1]
ax.plot(x, mfx_tri, 'k', linewidth=2.5)
ax.axvline(centroid_val, color='r', linestyle='--', label=f'Centroid = {centroid_val:.2f}')
ax.set_title('Centroid Method')
ax.set_ylim(-0.05, 1.05)
ax.legend()
ax.grid(True)

# Plot 3: Weighted Average
ax = axes[2]
low = fuzz.trimf(x, [0, 2, 5])
med = fuzz.trimf(x, [2, 5, 8])
high = fuzz.trimf(x, [5, 8, 10])
ax.plot(x, low, 'b', label='Low')
ax.plot(x, med, 'g', label='Medium')
ax.plot(x, high, 'm', label='High')
ax.axvline(wa_val, color='r', linestyle='--', label=f'Weighted Avg = {wa_val:.2f}')
ax.set_title('Weighted Average Method')
ax.set_ylim(-0.05, 1.05)
ax.legend()
ax.grid(True)

for ax in axes:
    ax.set_xlabel('Output Value')
    ax.set_ylabel('Membership Degree')

plt.tight_layout()
plt.show()

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Universe of discourse
x = np.arange(0, 10.1, 0.1)

# --- 1. Max-Membership Principle (MoM) ---
mfx_trap = fuzz.trapmf(x, [3, 5, 7, 9])
mom_val = fuzz.defuzz(x, mfx_trap, 'mom')

# --- 2. Centroid Method ---
mfx_tri = fuzz.trimf(x, [2, 5, 8])
centroid_val = fuzz.defuzz(x, mfx_tri, 'centroid')

# --- 3. Weighted Average Method ---
centers = np.array([2, 5, 8])
weights = np.array([0.4, 0.8, 0.6])
wa_val = np.sum(centers * weights) / np.sum(weights)

# Print results
print("--- Defuzzification Results ---")
print(f"MoM: {mom_val:.2f}")
print(f"Centroid: {centroid_val:.2f}")
print(f"Weighted Average: {wa_val:.2f}")

# Plot setup
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle('Defuzzification Methods (MoM | Centroid | Weighted Avg)', fontsize=14)

# Plot 1: MoM
ax = axes[0]
ax.plot(x, mfx_trap, 'k', linewidth=2.5)
ax.axvline(mom_val, color='g', linestyle='--', label=f'MoM = {mom_val:.2f}')
ax.set_title('Mean of Maximum (MoM)')
ax.set_ylim(-0.05, 1.05)
ax.legend()
ax.grid(True)

# Plot 2: Centroid
ax = axes[1]
ax.plot(x, mfx_tri, 'k', linewidth=2.5)
ax.axvline(centroid_val, color='r', linestyle='--', label=f'Centroid = {centroid_val:.2f}')
ax.set_title('Centroid Method')
ax.set_ylim(-0.05, 1.05)
ax.legend()
ax.grid(True)

# Plot 3: Weighted Average
ax = axes[2]
low = fuzz.trimf(x, [0, 2, 5])
med = fuzz.trimf(x, [2, 5, 8])
high = fuzz.trimf(x, [5, 8, 10])
ax.plot(x, low, 'b', label='Low')
ax.plot(x, med, 'g', label='Medium')
ax.plot(x, high, 'm', label='High')
ax.axvline(wa_val, color='r', linestyle='--', label=f'Weighted Avg = {wa_val:.2f}')
ax.set_title('Weighted Average Method')
ax.set_ylim(-0.05, 1.05)
ax.legend()
ax.grid(True)

for ax in axes:
    ax.set_xlabel('Output Value')
    ax.set_ylabel('Membership Degree')

plt.tight_layout()
plt.show()