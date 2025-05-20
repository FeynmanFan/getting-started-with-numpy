import numpy as np

# english thrust units - foot-pounds
burn_data = np.array([
    [140.0, 600], # [foot-pounds of thrust, duration in seconds]
    [140.0, 300], 
    [140.0, 900], 
])

# conversion factor
lbf_to_newton = 4.44822

forces_lbf = burn_data[:, 0]
times = burn_data[:, 1]

# column of corrected forces
forces_newton = forces_lbf * lbf_to_newton

converted_burn_data = np.column_stack((forces_newton, times))

original_impulse = burn_data[:, 0] * burn_data[:, 1]
correct_impulse = converted_burn_data[:, 0] * converted_burn_data[:, 1] 

print("Original Burn Data [Force (lbf), Time (s)]:\n", burn_data)
print("\nConverted Burn Data [Force (N), Time (s)]:\n", converted_burn_data)
print("\nOriginal Impulse (lbf·s, wrongly treated as N·s):", original_impulse)
print("Correct Impulse (N·s):", correct_impulse)
print("\nImpulse Error Factor (Original vs. Correct):",
      original_impulse / correct_impulse)