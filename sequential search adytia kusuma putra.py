class Barang:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama

def sequential_search(arr, x):
    for i in range(len(arr)):
        if arr[i].nama.lower() == x:
            return i
    return -1

def tambah_barang():
    kode = input("Masukkan kode sepatu: ")
    nama = input("Masukkan nama sepatu: ")
    return Barang(kode, nama)

def tampilkan_barang(daftar_barang):
    if not daftar_barang:
        print("Daftar barang kosong.")
    else:
        print("Daftar barang:")
        for i, barang in enumerate(daftar_barang):
            print(f"{i + 1}. Kode Sepatu: {barang.kode}, Nama Sepatu: {barang.nama}")

def main():
    daftar_barang = []

    while True:
        print("\nMenu:")
        print("1. Tambah barang sepatu")
        print("2. Tampilkan barang sepatu")
        print("3. Cari barang")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            barang_baru = tambah_barang()
            daftar_barang.append(barang_baru)
            print("Barang berhasil ditambahkan.")

        elif pilihan == '2':
            tampilkan_barang(daftar_barang)

        elif pilihan == '3':
            if not daftar_barang:
                print("Daftar barang kosong. Tambahkan barang terlebih dahulu.")
            else:
                nama_barang = input("Masukkan nama barang yang akan dicari: ").strip().lower()
                result = sequential_search(daftar_barang, nama_barang)
                if result != -1:
                    print(f"'{nama_barang}' ditemukan pada indeks {result}")
                else:
                    print(f"'{nama_barang}' tidak ditemukan dalam daftar barang.")

        elif pilihan == '4':
            print("Terima kasih!")
            break

        else:
            print("Menu tidak valid. Silakan pilih menu yang tersedia.")

if __name__ == "__main__":
    main()