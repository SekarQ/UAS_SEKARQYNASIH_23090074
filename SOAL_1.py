#buatlah sebuah program berdasarkan alur flowchart diatas
def main():
    mahasiswa = []

    while True:
        # Masukkan NIM dan Nama
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        
        # Simpan data mahasiswa
        mahasiswa.append({"NIM": nim, "Nama": nama})
        
        # Tanya apakah ingin menambah data lagi
        tambah_lagi = input("Ingin menambah lagi? (ya/tidak): ").lower()
        if tambah_lagi != 'ya':
            break

    # Tampilkan data mahasiswa
    print("\nData Mahasiswa:")
    for data in mahasiswa:
        print(f"NIM: {data['NIM']}, Nama: {data['Nama']}")

if __name__ == "__main__":
    main()
