import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
# Data
data = {
    'fx': [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
    'e^x': [0.006737947, 0.018315639, 0.049787068, 0.135335283, 0.367879441, 1, 2.718281828, 7.389056099, 20.08553692, 54.59815003, 148.4131591]
}

# Create DataFrame
df = pd.DataFrame(data)
# Print DataFrame with tabulate
print(tabulate(df, headers='keys', tablefmt='grid'))
# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df['fx'], df['e^x'], marker='o', color='orange')
plt.title('Plot of $e^x$')
plt.xlabel('fx')
plt.ylabel('$e^x$')

# Set Cartesian coordinate grid lines
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, which='both')

plt.show()
