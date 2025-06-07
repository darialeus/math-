import numpy as np
import matplotlib.pyplot as plt

def f(x):
    # Define the function you want to integrate
    return np.cos(8*x)  # Example function x^3

def monte_carlo_integration(f, a, b, num_points):
    # Perform probabilistic Monte Carlo integration
    min_f = np.min(f(np.linspace(a, b, 1000)))
    max_f = np.max(f(np.linspace(a, b, 1000)))

    total_area = 0
    for _ in range(num_points):
        x = np.random.uniform(a, b)
        y = np.random.uniform(min_f, max_f)
        if 0 <= y <= np.abs(f(x)):
            total_area += 1 if f(x) >= 0 else -1
    return total_area / num_points * (b - a) * (max_f - min_f)

def plot_integration(f, a, b, num_points):
    # Plot the function and the random points used for integration
    x = np.linspace(a, b, 1000)
    y = f(x)
    plt.plot(x, y, label='Function: f(x)')

    min_f = np.min(y)
    max_f = np.max(y)
    random_x = np.random.uniform(a, b, num_points)
    random_y = np.random.uniform(min_f, max_f, num_points)
    below_x = random_x[np.abs(random_y) <= np.abs(f(random_x))]
    below_y = random_y[np.abs(random_y) <= np.abs(f(random_x))]
    plt.scatter(below_x, below_y, color='red', alpha=0.5, label='Points Below Curve')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Probabilistic Monte Carlo Integration')
    plt.legend()
    plt.grid(True)
    plt.show()

# Define integration limits
a = 0
b = 2*np.pi/3.

# Number of random points for Monte Carlo integration
num_points = 1000

# Perform Monte Carlo integration
integral = monte_carlo_integration(f, a, b, num_points)
print("Monte Carlo Integration Result:", integral)

# Plot the function and the random points
plot_integration(f, a, b, num_points)
