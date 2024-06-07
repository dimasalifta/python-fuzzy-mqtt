import matplotlib.pyplot as plt
import numpy as np

# Defining the ranges
x = np.linspace(0, 100, 500)

# Defining the membership functions
def normal(x):
    return np.where(x <= 20, 1, np.where(x <= 30, (30 - x) / 10, 0))

def sedang(x):
    return np.where((20 < x) & (x <= 30), (x - 20) / 10, np.where((30 < x) & (x <= 50), 1, np.where((50 < x) & (x <= 60), (60 - x) / 10, 0)))

def tinggi(x):
    return np.where(x <= 50, 0, np.where(x <= 60, (x - 50) / 10, 1))

# Apply the functions to the range x
normal_values = normal(x)
sedang_values = sedang(x)
tinggi_values = tinggi(x)

# Plotting the fuzzy membership functions
plt.figure(figsize=(10, 6))
plt.plot(x, normal_values, label='Normal (N)')
plt.plot(x, sedang_values, label='Sedang (S)')
plt.plot(x, tinggi_values, label='Tinggi (T)')

plt.title('Fuzzy Membership Functions')
plt.xlabel('Nilai (PPM)')
plt.ylabel('Degree of Membership')
plt.legend(loc='best')
plt.grid(True)
plt.show()
