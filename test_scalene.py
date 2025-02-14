import time

# Sample functions with different complexities
def constant_time(n):
    return 42  # O(1)

def linear_time(n):
    return [i**2 for i in range(n)]  # O(n)

def quadratic_time(n):
    return [[i * j for j in range(n)] for i in range(n)]  # O(n^2)

# Run functions with increasing input size
n = 1000
constant_time(n)
linear_time(n)
quadratic_time(n)

# Add sleep to simulate real-world processing
time.sleep(2)
