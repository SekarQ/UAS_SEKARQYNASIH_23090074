# Parent class
class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    def set_nama(self, nama):
        self.nama = nama

    def set_warna(self, warna):
        self.warna = warna

    def set_rasa(self, rasa):
        self.rasa = rasa

    def information(self):
        return f"Nama: {self.nama}, Warna: {self.warna}, Rasa: {self.rasa}"

# Child class
class Mangga(Buah):
    def __init__(self, nama, warna, rasa, vitamin):
        super().__init__(nama, warna, rasa)
        self.vitamin = vitamin

    def set_vitamin(self, vitamin):
        self.vitamin = vitamin

    def information(self):
        parent_info = super().information()
        return f"{parent_info}, Vitamin: {self.vitamin}"

mangga1 = Mangga("Mangga Harum Manis", "Hijau", "Manis", "Vitamin C")
print(mangga1.information())

mangga1.set_nama("Mangga Gedong")
mangga1.set_warna("Kuning")
mangga1.set_rasa("Manis dan Sedikit Asam")
mangga1.set_vitamin("Vitamin A dan C")
print(mangga1.information())
