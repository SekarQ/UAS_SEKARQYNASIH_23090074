# buatlah sebuah program sistem antrian restoran dengan menggunakan class untuk mengelola antrian pesanan. program ini harus memiliki dua fungsi untuk menangani antrian pesanan yaitu :
# Enqueue : fungsi untuk menambahkan pesanan baru ke dalam antrian
# Dequeue : fungsi untuk menghapus antrian dari depan
# implementasikan program ini menggunakan class dan jalankan program dalam modul python terpisah

class RestaurantQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, order):
        self.queue.append(order)
        print(f"Order '{order}' telah di tambahkan.")

    def dequeue(self):
        if len(self.queue) > 0:
            order = self.queue.pop(0)
            print(f"Order '{order}' telah di hapus")
            return order
        else:
            print("tidak ada orderan yang akan di hapus.")
            return None

    def display_queue(self):
        if len(self.queue) > 0:
            print("Current queue:", self.queue)
        else:
            print("kosong.")

if __name__ == "__main__":
    restaurant_queue = RestaurantQueue()

    while True:
        print("\nRestaurant Order Queue System")
        print('   ')
        print("1. masukan pesanan ke dalam antrian")
        print("2. hapus orderan dari antrian")
        print("3. lihat pesananan yang telah di tambahkan")
        print("4. keluar")
        print('   ')

        choice = input("masukan pilihan anda: ")

        if choice == '1':
            order = input("masukan pesanan anda: ")
            restaurant_queue.enqueue(order)
        elif choice == '2':
            restaurant_queue.dequeue()
        elif choice == '3':
            restaurant_queue.display_queue()
        elif choice == '4':
            print("keluar dari program.")
            break
        else:
            print("gagal, silahkan coba lagi.")


