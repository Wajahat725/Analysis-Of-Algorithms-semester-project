import random

# Objective function: minimize x^2 + y^2
def objective_function(x):
    return x[0]**2 + x[1]**2

# Harmony Search Parameters
HMS = 5                # Harmony Memory Size
HMCR = 0.9             # Harmony Memory Consideration Rate
PAR = 0.3              # Pitch Adjustment Rate
BW = 0.01              # Bandwidth (small changes)
max_iter = 1000        # Number of iterations
bounds = [(-5, 5), (-5, 5)]  # Bounds for x and y

# Step 1: Initialize Harmony Memory (HM)
harmony_memory = []
for _ in range(HMS):
    harmony = [random.uniform(b[0], b[1]) for b in bounds]
    harmony_memory.append((harmony, objective_function(harmony)))

# Step 2: Harmony Search Loop
for it in range(max_iter):
    new_harmony = []
    for i in range(len(bounds)):
        if random.random() < HMCR:
            # Choose value from memory
            value = random.choice(harmony_memory)[0][i]
            if random.random() < PAR:
                # Pitch adjustment
                value += random.uniform(-BW, BW)
        else:
            # Random value
            value = random.uniform(bounds[i][0], bounds[i][1])
        new_harmony.append(value)

    new_score = objective_function(new_harmony)

    # Replace worst harmony if new one is better
    worst_index = max(range(HMS), key=lambda i: harmony_memory[i][1])
    if new_score < harmony_memory[worst_index][1]:
        harmony_memory[worst_index] = (new_harmony, new_score)

# Step 3: Return best harmony
best_harmony = min(harmony_memory, key=lambda x: x[1])
print("Best solution:", best_harmony[0])
print("Best score:", best_harmony[1])
