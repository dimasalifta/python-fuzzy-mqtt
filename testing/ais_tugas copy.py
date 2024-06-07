import numpy as np
from tabulate import tabulate
import pandas as pd
import matplotlib.pyplot as plt
# Create the sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
# Data
data = {
    'fx': [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
    'e^x': [0.006737947, 0.018315639, 0.049787068, 0.135335283, 0.367879441, 1, 2.718281828, 7.389056099, 20.08553692, 54.59815003, 148.4131591]
}

# Create DataFrame
df = pd.DataFrame(data)

# Print DataFrame with tabulate
print(tabulate(df, headers='keys', tablefmt='grid'))
# Apply the sigmoid function to the fx values
data['sigmoid'] = sigmoid(np.array(data['fx']))

# Create DataFrame
df_sigmoid = pd.DataFrame(data)

# Print DataFrame with sigmoid values using tabulate
print(tabulate(df_sigmoid[['fx', 'sigmoid']], headers='keys', tablefmt='grid'))

# Plotting the sigmoid function
plt.figure(figsize=(10, 6))
plt.plot(df_sigmoid['fx'], df_sigmoid['sigmoid'], marker='o', color='orange')
plt.title('Plot of Sigmoid Function')
plt.xlabel('fx')
plt.ylabel('Sigmoid(fx)')

# Set Cartesian coordinate grid lines
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, which='both')

plt.show()
