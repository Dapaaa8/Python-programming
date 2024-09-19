# Harga tiket berdasarkan kategori usia
harga_anak = 30000
harga_dewasa = 50000
harga_lansia = 35000

# Meminta input jumlah pembeli tiket
jumlah_pembeli= int(input("masukan jumlah pembeli tiket: "))

# Variabel untuk menyimpan total
total_harga = 0

# Loop untuk setiap pembeli
for i in range(jumlah_pembeli):
    print(f"\nPembeli{i+1}:")

# Meminta input usia pembeli
usia = int(input("masukan usia pembeli: "))

# Meminta input jumlah tiket yang dibeli
jumlah_tiket = int(input("masukan jumlah tiket yang ingin dibeli: "))

# Menentukan harga tiket berdasarkan usia
if usia < 12:
    harga_tiket = harga_anak
elif usia <= 60:
    harga_tiket = harga_dewasa
else
    harga_tiket = harga_lansia

# Menghitung total harga tiket untuk pembeli hari ini
total_harga_pembeli = harga_tiket * jumlah_tiket
total_harga += total_harga_pembeli

# Menampilkan harga tiket per orang
   print("harga tiket untuk pembeli{i+1}:Rp{total_harga_pembeli}")

# Menampilkan total harga untuk semua tiket yang dibeli
   print(f"\nTotal harga untuk semua tiket yang dibeli:Rp{total_harga}")