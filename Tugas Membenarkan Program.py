def binary_search(arr, x):
    
    low = 0 
    high = len(arr) -1 
    mid = 0
    
    while low <= high:
        mid = (high + low ) // 2
        
        # jika elemen berada di tengah 
        if arr[mid] < x:
            low = mid + 1
            
        #jika elemen berada di sebelah kiri tengah 
        elif arr[mid] > x:
            high = mid - 1
            
        #elemen di temukan 
        else:
            return mid
            
        #elemen tidak di temukan 
    return -1
            
def main ():
    #menerima input daftar elemen yang sudah terurut dari pengguna 
    arr = list(map(int, input('Masukan daftar elemen yang sudah terurut (pisahkan dengan spasi):').split()))
    
    #menerima input elemen yang akan dicari 
    x = int(input('Masukan elemen yang di cari : '))
    
    result = binary_search(arr, x)
    
    if result != -1:
        print(f"elemen di temukan pada indeks{result}")
        
    else:
        print("elemen tidak di temukan dalam daftar")
        
    #menjalankan fungsi utaman 
if __name__ == "__main__":
    main()