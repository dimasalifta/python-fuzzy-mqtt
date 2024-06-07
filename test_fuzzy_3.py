class SistemFuzzy:
    def __init__(self, kelembaban, amoniak):
        self.kelembaban = kelembaban
        self.amoniak = amoniak
        self.basah = 0
        self.lembab = 0
        self.kering = 0
        self.normal = 0
        self.sedang = 0
        self.tinggi = 0
        self.hasil = ""

    def kelembaban_basah(self):
        if self.kelembaban <= 65:
            self.basah = 0
        elif 65 < self.kelembaban < 85:
            self.basah = (self.kelembaban - 65) / 20
        elif self.kelembaban >= 85:
            self.basah = 1
        return self.basah

    def kelembaban_lembab(self):
        if self.kelembaban <= 25:
            self.lembab = 0
        elif 25 <= self.kelembaban <= 45:
            self.lembab = (self.kelembaban - 25) / 20
        elif 65 < self.kelembaban <= 85:
            self.lembab = (85 - self.kelembaban) / 20
        elif 45 <= self.kelembaban <= 65:
            self.lembab = 1
        return self.lembab

    def kelembaban_kering(self):
        if self.kelembaban <= 25:
            self.kering = 1
        elif 25 < self.kelembaban < 45:
            self.kering = (45 - self.kelembaban) / 20
        elif self.kelembaban >= 45:
            self.kering = 0
        return self.kering

    def amoniak_normal(self):
        if self.amoniak <= 20:
            self.normal = 1
        elif 20 < self.amoniak < 30:
            self.normal = (30 - self.amoniak) / 10
        elif self.amoniak >= 30:
            self.normal = 0
        return self.normal

    def amoniak_sedang(self):
        if self.amoniak <= 20 or self.amoniak >= 60:
            self.sedang = 0
        elif 20 <= self.amoniak <= 30:
            self.sedang = (self.amoniak - 20) / 10
        elif 50 < self.amoniak <= 60:
            self.sedang = (60 - self.amoniak) / 10
        elif 30 <= self.amoniak <= 50:
            self.sedang = 1
        return self.sedang

    def amoniak_tinggi(self):
        if self.amoniak >= 60:
            self.tinggi = 1
        elif 50 < self.amoniak < 60:
            self.tinggi = (self.amoniak - 50) / 10
        elif self.amoniak <= 50:
            self.tinggi = 0
        return self.tinggi

    def fuzzifikasi(self):
        self.kelembaban_basah()
        self.kelembaban_lembab()
        self.kelembaban_kering()
        self.amoniak_normal()
        self.amoniak_sedang()
        self.amoniak_tinggi()

    def defuzzifikasi(self):
        centroid_kering = 10  # Centroid untuk himpunan kering (berdasarkan kelembaban)
        centroid_lembab = 55  # Centroid untuk himpunan lembab (berdasarkan kelembaban)
        centroid_basah = 92.5  # Centroid untuk himpunan basah (berdasarkan kelembaban)

        centroid_normal = 10  # Centroid untuk himpunan normal (berdasarkan amoniak)
        centroid_sedang = 35  # Centroid untuk himpunan sedang (berdasarkan amoniak)
        centroid_tinggi = 75  # Centroid untuk himpunan tinggi (berdasarkan amoniak)

        # Hitung nilai crisp dengan metode centroid
        nilai_crisp_kelembaban = (self.basah * centroid_basah + self.lembab * centroid_lembab + self.kering * centroid_kering) / (
                    self.basah + self.lembab + self.kering)
        nilai_crisp_amoniak = (self.normal * centroid_normal + self.sedang * centroid_sedang + self.tinggi * centroid_tinggi) / (
                    self.normal + self.sedang + self.tinggi)

        # Gabungkan kedua nilai crisp ke dalam nilai akhir
        nilai_crisp_total = (nilai_crisp_kelembaban + nilai_crisp_amoniak) / 2  # Rata-rata kedua nilai crisp
        print(nilai_crisp_total)
        # Tentukan hasil berdasarkan nilai crisp total
        if nilai_crisp_total <= 20:
            self.hasil = "AMAN"
        elif 20 < nilai_crisp_total <= 40:
            self.hasil = "WASPADA"
        elif 40 < nilai_crisp_total <= 100:
            self.hasil = "BAHAYA"

        return self.hasil


# Contoh penggunaan
kelembaban_input = 100
amoniak_input = 0

sistem_fuzzy = SistemFuzzy(kelembaban_input, amoniak_input)
sistem_fuzzy.fuzzifikasi()
hasil_defuzzifikasi = sistem_fuzzy.defuzzifikasi()

print("Hasil defuzzifikasi:", hasil_defuzzifikasi)
