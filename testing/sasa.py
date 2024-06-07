import numpy as np
import matplotlib.pyplot as plt

# Definisi fungsi keanggotaan
def normal(x):
    if x <= 0 or x >= 30:
        return 0
    elif 0 < x < 20:
        return (x - 0) / (20 - 0)
    elif 20 <= x <= 30:
        return (30 - x) / (30 - 20)
    
def sedang(x):
    if x <= 20 or x >= 60:
        return 0
    elif 20 < x < 30:
        return (x - 20) / (30 - 20)
    elif 30 <= x <= 50:
        return (50 - x) / (50 - 30)
    elif 50 < x < 60:
        return (60 - x) / (60 - 50)
    
def tinggi(x):
    if x <= 50:
        return 0
    elif 50 <= x < 60:
        return (x - 50) / (60 - 50)
    elif x >= 80:
        return 1

# Range nilai x untuk plotting
x = np.linspace(0, 100, 1000)

# Menghitung nilai keanggotaan untuk setiap fungsi
y_normal = [normal(i) for i in x]
y_sedang = [sedang(i) for i in x]
y_tinggi = [tinggi(i) for i in x]

# Plot fungsi keanggotaan
plt.figure(figsize=(10, 6))
plt.plot(x, y_normal, label='Normal')
plt.plot(x, y_sedang, label='Sedang')
plt.plot(x, y_tinggi, label='Tinggi')
plt.title('Fungsi Keanggotaan')
plt.xlabel('Nilai')
plt.ylabel('Keanggotaan')
plt.legend()
plt.grid(True)
plt.show()
s