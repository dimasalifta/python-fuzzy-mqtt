import matplotlib.pyplot as plt
import numpy as np
import math
# Data kelembaban
nilai_linguistik_kelembaban = {
    "rendah":np.arange(20),
    "sedang":np.arange(20,50+1),
    "tinggi":np.arange(50,100+1)
    
}
centroid_kelembaban = {
    "rendah":np.median(nilai_linguistik_kelembaban['rendah']),
    "sedang":np.median(nilai_linguistik_kelembaban['sedang']),
    "tinggi":np.median(nilai_linguistik_kelembaban['tinggi'])
}

    
# Fungsi keanggotaan fuzzy untuk setiap kategori kelembaban
def rendah():
    if x <= 20:
        return 1
    elif x > 20 and x < 35:
        return (35 - x) / 15
    else:
        return 0

def sedang(x):
    if x <= 20 or x >= 80:
        return 0
    elif x > 20 and x <= 50:
        return (x - 20) / 30
    elif x > 50 and x < 70:
        return (70 - x) / 20
    else:
        return 0

def tinggi(x):
    if x <= 50:
        return 0
    elif x > 50 and x < 75:
        return (x - 50) / 25
    else:
        return 1

# Persentase kelembaban relatif
x = np.arange(0, 101, 1)

# Menggambar grafik keanggotaan fuzzy
plt.figure(figsize=(10, 6))

plt.plot(x, [rendah(i) for i in x], label='Rendah')
plt.plot(x, [sedang(i) for i in x], label='Sedang')
plt.plot(x, [tinggi(i) for i in x], label='Tinggi')

plt.title('Grafik Keanggotaan Fuzzy Kelembaban')
plt.xlabel('Persentase Kelembaban Relatif (%)')
plt.ylabel('Derajat Keanggotaan')
plt.legend()
plt.grid(True)
plt.show()
