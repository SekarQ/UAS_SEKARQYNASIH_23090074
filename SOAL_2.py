# nama : algoritma dan struktur data 2 : matematika numerik
# mahasiswa 1 : 90 : 80
# mahasiswa 2 : 50 : 60
# mahasiswa 3 : 65 : 70
# buatlah sebuah array 2 dimensi yang berisi data pada tabel di atas dalam bentuk dataframe lalu, buatlah program untuk melakukan operasi berikut :
# tampilkan rata rata nilai untuk setiap mata kuliah 
# tampilkan rata rata nilai untuk setiap mahasiswa

import pandas as pd

# Membuat DataFrame dari data yang diberikan
data = {
    "Nama": ["Mahasiswa 1", "Mahasiswa 2", "Mahasiswa 3"],
    "Algoritma dan Struktur Data 2": [90, 50, 65],
    "Matematika Numerik": [80, 60, 70]
}

df = pd.DataFrame(data)

# Menampilkan DataFrame
print("Data Mahasiswa:")
print(df)

# 1. menghitung rata-rata nilai untuk setiap mata kuliah
rata_rata_mata_kuliah = df.mean(axis=0, numeric_only=True)
print("\nRata-rata nilai untuk setiap mata kuliah:")
print(rata_rata_mata_kuliah)

# 2. menghitung rata-rata nilai untuk setiap mahasiswa
df["Rata-rata"] = df.mean(axis=1, numeric_only=True)
print("\nData Mahasiswa dengan Rata-rata:")
print(df)

rata_rata_mahasiswa = df[["Nama", "Rata-rata"]]
print("\nRata-rata nilai untuk setiap mahasiswa:")
print(rata_rata_mahasiswa)
