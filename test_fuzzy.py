class FuzzyLogic:
    def __init__(self, kelembaban, amoniak):
        self.kelembaban = kelembaban
        self.amoniak = amoniak
        self.basah = 0.0
        self.lembab = 0.0
        self.kering = 0.0
        self.Normal = 0.0
        self.Sedang = 0.0
        self.Tinggi = 0.0
        self.RESULT = ""

    def kelembabanbasah(self):
        if self.kelembaban >= 85:
            self.basah = 1
        elif 65 < self.kelembaban < 85:
            self.basah = (self.kelembaban - 65) / 20
        else:
            self.basah = 0
        return self.basah

    def kelembabanlembab(self):
        if 45 <= self.kelembaban <= 65:
            self.lembab = 1
        elif 65 < self.kelembaban < 85:
            self.lembab = (85 - self.kelembaban) / 20
        elif 25 <= self.kelembaban < 45:
            self.lembab = (self.kelembaban - 25) / 20
        else:
            self.lembab = 0
        return self.lembab

    def kelembabankering(self):
        if self.kelembaban <= 25:
            self.kering = 1
        elif 25 < self.kelembaban < 45:
            self.kering = (45 - self.kelembaban) / 20
        else:
            self.kering = 0
        return self.kering

    def amoniakNormal(self):
        if self.amoniak <= 20:
            self.Normal = 1
        elif 20 < self.amoniak < 30:
            self.Normal = (30 - self.amoniak) / 10
        else:
            self.Normal = 0
        return self.Normal

    def amoniakSedang(self):
        if 20 <= self.amoniak < 30:
            self.Sedang = (self.amoniak - 20) / 10
        elif 30 <= self.amoniak <= 50:
            self.Sedang = 1
        elif 50 < self.amoniak < 60:
            self.Sedang = (60 - self.amoniak) / 10
        else:
            self.Sedang = 0
        return self.Sedang

    def amoniakTinggi(self):
        if self.amoniak >= 60:
            self.Tinggi = 1
        elif 50 < self.amoniak < 60:
            self.Tinggi = (self.amoniak - 50) / 10
        else:
            self.Tinggi = 0
        return self.Tinggi

    def fuzzifikasi(self):
        self.kelembabanbasah()
        self.kelembabanlembab()
        self.kelembabankering()
        self.amoniakNormal()
        self.amoniakSedang()
        self.amoniakTinggi()
        print(f"basah: {self.basah}\t lembab: {self.lembab}\t kering: {self.kering}")
        print(f"Normal: {self.Normal}\t sedang: {self.Sedang}\t Tinggi: {self.Tinggi}")

    def defuzzifikasi(self):
        if self.Normal > 0.5 and self.kering > 0.5:
            self.RESULT = "AMAN"
        elif self.Normal > 0.5 and self.lembab > 0.5:
            self.RESULT = "AMAN"
        elif self.Sedang > 0.5 and self.kering > 0.5:
            self.RESULT = "AMAN"
        elif self.Normal > 0.5 and self.basah > 0.5:
            self.RESULT = "WASPADA"
        elif self.Sedang > 0.5 and self.lembab > 0.5:
            self.RESULT = "WASPADA"
        elif self.Tinggi > 0.5 and self.kering > 0.5:
            self.RESULT = "WASPADA"
        elif self.Sedang > 0.5 and self.basah > 0.5:
            self.RESULT = "BAHAYA"
        elif self.Tinggi > 0.5 and self.lembab > 0.5:
            self.RESULT = "BAHAYA"
        elif self.Tinggi > 0.5 and self.basah > 0.5:
            self.RESULT = "BAHAYA"

        print(f"Status: {self.RESULT}")
        print("=========================================================================")
        self.control_output()

    def control_output(self):
        if self.RESULT == "BAHAYA":
            print("LED Merah: ON, LED Hijau: OFF, Relay: ON")
        elif self.RESULT == "WASPADA":
            print("LED Merah: ON, LED Hijau: OFF, Relay: OFF")
        elif self.RESULT == "AMAN":
            print("LED Merah: OFF, LED Hijau: ON, Relay: OFF")

# Example usage
kelembaban = 15  # Replace with actual sensor reading
amoniak = 1    # Replace with actual sensor reading

fuzzy_logic = FuzzyLogic(kelembaban, amoniak)

print("\tFuzzifikasi")
fuzzy_logic.fuzzifikasi()

print("\tDefuzzifikasi")
fuzzy_logic.defuzzifikasi()
