# name - kushagra
# roll number-24134003
# batch-P745
# solving assigment 0 2nd problem
#  Geometric Progression (GP) 
initial_term_gp = 1.25      # First term of the GP
common_ratio = 0.5          # Common ratio of the GP
num_terms = 15              # Number of terms to generate

print("Geometric Progression (GP) terms:")
gp_sum = 0.0

# Generate GP terms and calculate the sum
for i in range(num_terms):
    current_term = initial_term_gp * (common_ratio ** i)
    print(f"{current_term:.4f}", end=" ")
    gp_sum += current_term

print(f"\nSum of first {num_terms} GP terms: {gp_sum:.4f}")

# --- Harmonic Progression (HP) setup ---
# HP is defined as the reciprocal of an Arithmetic Progression (AP)
initial_term_ap = 1.25      # First term of the underlying AP
common_difference = 1.5     # Common difference of the AP

print("\nHarmonic Progression (HP) terms:")
hp_sum = 0.0

# Generate HP terms and calculate the sum
for i in range(num_terms):
    ap_term = initial_term_ap + i * common_difference
    hp_term = 1.0 / ap_term
    print(f"{hp_term:.4f}", end=" ")
    hp_sum += hp_term

print(f"\nSum of first {num_terms} HP terms: {hp_sum:.4f}")
