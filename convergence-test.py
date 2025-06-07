import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the sequence (1 + 1/n)^n
def calculate_sequence(n_values):
    return [(1 + 1/n)**n for n in n_values]

# Calculate the actual value of e
e = np.exp(1)

# Define the range of n values
n_values = np.arange(1, 1000)

# Calculate the sequence values
sequence_values = calculate_sequence(n_values)

# Plot the convergence of the sequence
plt.figure(figsize=(10, 5))
plt.plot(n_values, sequence_values, label='Sequence (1 + 1/n)^n')
plt.axhline(y=e, color='r', linestyle='--', label='Actual value of e')
plt.xlabel('n')
plt.xlim(1,10)
plt.ylabel('Sequence value')
plt.title('Convergence of the sequence (1 + 1/n)^n to e')
plt.legend()
plt.grid(True)
plt.show()

# Calculate the error between each element of the sequence and e
errors = 100*np.abs(np.array(sequence_values) - e)/e

# Plot the error
plt.figure(figsize=(10, 5))
plt.xlim(0,50)
plt.ylim(0,25)
plt.plot(n_values, errors, label='Error')
plt.xlabel('n')
plt.ylabel('Error')
plt.title('Error between sequence value and actual value of e, in per cent')
plt.legend()
plt.grid(True)
plt.show()
