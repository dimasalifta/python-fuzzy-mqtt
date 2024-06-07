import json

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
        
        fuzzyfikasi_data = {
            "kering": self.kering,
            "lembab": self.lembab,
            "basah": self.basah,
            "normal": self.normal,
            "sedang": self.sedang,
            "tinggi": self.tinggi,
        }
        fuzzyfikasi_data = json.dumps(fuzzyfikasi_data, indent=4)
        print(f"basah: {self.basah}\tlembab: {self.lembab}\tkering: {self.kering}")
        print(f"Normal: {self.normal}\tsedang: {self.sedang}\tTinggi: {self.tinggi}")
        return fuzzyfikasi_data

    def inference(self):
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
        status = {
            "STATUS": self.hasil
        }
        
        status_json = json.dumps(status, indent=4)
        print(f"HASIL: {status_json}")
        return status_json

    def defuzzyfikasi(self):
        # Define the centroids of the output sets
        output_values = {
            "AMAN": 25,
            "WASPADA": 50,
            "BAHAYA": 75,
            "TIDAK TERDEFINISI": 0
        }

        # Get the inferred status
        status = self.inference()
        print
        status_dict = json.loads(status)
        inferred_status = status_dict["STATUS"]

        # Perform defuzzification using the centroid method
        crisp_value = output_values.get(inferred_status, 0)

        defuzzyfikasi_data = {
            "crisp_value": crisp_value
        }
        defuzzyfikasi_json = json.dumps(defuzzyfikasi_data, indent=4)
        print(f"Defuzzifikasi crisp value: {crisp_value}")
        return defuzzyfikasi_json

# Example usage:
sistem = SistemFuzzy(kelembaban=70, amoniak=0)
sistem.fuzzifikasi()
sistem.inference()
sistem.defuzzyfikasi()
