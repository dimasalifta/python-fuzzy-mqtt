import numpy as np
import matplotlib.pyplot as plt

# Definisikan fungsi keanggotaan
def trapezoidal_function(x, a, b, c, d):
    if x <= a or x >= d:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x <= c:
        return 1
    elif c < x < d:
        return (d - x) / (d - c)

# Definisikan rentang nilai x
x = np.linspace(0, 100,1000)

# Definisikan parameter fungsi keanggotaan untuk kategori kering
a_kering, b_kering, c_kering, d_kering = 0, 0, 20, 30
y_kering = [trapezoidal_function(i, a_kering, b_kering, c_kering, d_kering) for i in x]

# Definisikan parameter fungsi keanggotaan untuk kategori lembab
a_lembab, b_lembab, c_lembab, d_lembab = 20, 30, 50, 60
y_lembab = [trapezoidal_function(i, a_lembab, b_lembab, c_lembab, d_lembab) for i in x]

# Definisikan parameter fungsi keanggotaan untuk kategori basah
a_basah, b_basah, c_basah, d_basah = 50, 60, 80, 100
y_basah = [trapezoidal_function(i, a_basah, b_basah, c_basah, d_basah) for i in x]

# Definisikan parameter fungsi keanggotaan untuk kategori ammonia
a_ammonia, b_ammonia, c_ammonia, d_ammonia = 0, 0, 25, 45
y_ammonia = [trapezoidal_function(i, a_ammonia, b_ammonia, c_ammonia, d_ammonia) for i in x]

# Plot fungsi keanggotaan untuk setiap kategori
plt.plot(x, y_kering, label='Kering')
plt.plot(x, y_lembab, label='Lembab')
plt.plot(x, y_basah, label='Basah')
# plt.plot(x, y_ammonia, label='Ammonia')

# Tampilkan legenda
plt.legend()

# Tampilkan plot
plt.title('Fungsi Keanggotaan Trapesium')
plt.xlabel('Nilai Input')
plt.ylabel('Nilai Keanggotaan')
plt.grid(True)
plt.show()
