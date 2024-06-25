def binary_search(products, target_budget):
    """
    Fungsi untuk melakukan binary search pada daftar produk berdasarkan anggaran.
    
    Parameters:
    products (list of dict): Daftar produk yang sudah diurutkan berdasarkan harga produk.
    target_budget (int): Anggaran yang ingin dicari.
    
    Returns:
    list of dict: Daftar produk yang sesuai dengan anggaran.
    """
    left, right = 0, len(products) - 1
    matching_products = []

    while left <= right:
        mid = (left + right) // 2
        mid_price = products[mid]['price']
        
        if mid_price <= target_budget:
            # Tambahkan semua produk dari awal hingga mid ke daftar hasil
            matching_products = products[:mid + 1]
            left = mid + 1
        else:
            right = mid - 1
    
    return matching_products

# Daftar produk dalam toko, sudah diurutkan berdasarkan harga produk
products = [
    {'id': 115, 'name': 'Charger', 'price': 100000},
    {'id': 114, 'name': 'USB Flash Drive', 'price': 150000},
    {'id': 107, 'name': 'Mouse', 'price': 200000},
    {'id': 106, 'name': 'Keyboard', 'price': 300000},
    {'id': 110, 'name': 'Webcam', 'price': 400000},
    {'id': 111, 'name': 'Router', 'price': 600000},
    {'id': 112, 'name': 'Speaker', 'price': 800000},
    {'id': 105, 'name': 'Headphone', 'price': 750000},
    {'id': 113, 'name': 'External Hard Drive', 'price': 1000000},
    {'id': 109, 'name': 'Printer', 'price': 1200000},
    {'id': 104, 'name': 'Smartwatch', 'price': 1500000},
    {'id': 108, 'name': 'Monitor', 'price': 2000000},
    {'id': 103, 'name': 'Tablet', 'price': 3000000},
    {'id': 102, 'name': 'Smartphone', 'price': 5000000},
    {'id': 101, 'name': 'Laptop', 'price': 15000000},
]

# Fungsi untuk menampilkan menu utama
def show_menu():
    print("\nMenu Toko:")
    print("1. Cari produk berdasarkan uang")
    print("2. Tampilkan produk yang ada")
    print("3. Keluar")

# Fungsi untuk mencari produk berdasarkan anggaran
def search_by_budget():
    try:
        target_budget = int(input("Masukkan jumlah uang yang ingin Anda gunakan: "))
    except ValueError:
        print("Jumlah uang harus berupa angka.")
        return

    matching_products = binary_search(products, target_budget)

    if matching_products:
        print("Produk yang ditemukan sesuai anggaran:")
        for product in matching_products:
            print(f"ID: {product['id']}, Nama: {product['name']}, Harga: {product['price']}")
    else:
        print(f"Tidak ada produk yang sesuai dengan anggaran {target_budget}")

# Fungsi untuk menampilkan semua produk yang ada di dalam array
def display_products():
    if products:
        print("Produk yang tersedia di toko:")
        for product in products:
            print(f"ID: {product['id']}, Nama: {product['name']}, Harga: {product['price']}")
    else:
        print("Tidak ada produk yang tersedia.")

# Fungsi utama untuk menjalankan program
def main():
    while True:
        show_menu()
        try:
            choice = int(input("Pilih menu: "))
        except ValueError:
            print("Pilihan harus berupa angka.")
            continue

        if choice == 1:
            search_by_budget()
        elif choice == 2:
            display_products()
        elif choice == 3:
            print("Terima kasih telah membeli barang di toko kami!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()