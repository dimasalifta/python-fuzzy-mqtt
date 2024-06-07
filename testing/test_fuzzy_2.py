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
            self.basah = (self.kelembaban-65) / 20
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
            self.kering = (45-self.kelembaban) / 20
        elif self.kelembaban >= 45:
            self.kering = 0
        return self.kering

    def amoniak_normal(self):
        if self.amoniak <= 20:
            self.normal = 1
        elif 20 < self.amoniak < 30:
            self.normal = (30-self.amoniak) / 10
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
        else:
            print("masuk")
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
        print(f"basah: {self.basah}\tlembab: {self.lembab}\tkering: {self.kering}")
        print(f"Normal: {self.normal}\tsedang: {self.sedang}\tTinggi: {self.tinggi}")

    def defuzzifikasi(self):
        if self.normal >= 0.5 and self.kering >= 0.5:
            self.hasil = "AMAN"
        elif self.normal >= 0.5 and self.lembab >= 0.5:
            self.hasil = "AMAN"
        elif self.sedang >= 0.5 and self.kering >= 0.5:
            self.hasil = "AMAN"
        elif self.normal >= 0.5 and self.basah >= 0.5:
            self.hasil = "WASPADA"
        elif self.sedang >= 0.5 and self.lembab >= 0.5:
            self.hasil = "WASPADA"
        elif self.tinggi >= 0.5 and self.kering >= 0.5:
            self.hasil = "WASPADA"
        elif self.sedang >= 0.5 and self.basah >= 0.5:
            self.hasil = "BAHAYA"
        elif self.tinggi >= 0.5 and self.lembab >= 0.5:
            self.hasil = "BAHAYA"
        elif self.tinggi >= 0.5 and self.basah >= 0.5:
            self.hasil = "BAHAYA"
        else:
            self.hasil = "TIDAK TERDEFINISI"
        print(f"HASIL: {self.hasil}")

# Contoh penggunaan
sistem_fuzzy = SistemFuzzy(kelembaban=0, amoniak=50)  # Atur beberapa nilai tes
sistem_fuzzy.fuzzifikasi()
sistem_fuzzy.defuzzifikasi()