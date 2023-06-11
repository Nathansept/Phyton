""" Nathan Septian """
""" Membuat Program untuk menambah stok gudang """
nama = input("Masukkan Nama: ")

print("\nStok Gudang Input Barang")
print("###########################")
print("\nSelamat Datang", nama)
nama_barang = input("\nMasukkan nama barang yang mau ditambah : ")
jumlah_barang = int(input("\nMasukkan jumlah barang yang mau ditambah : "))
harga_beli = float(input("\nMasukkan harga beli untuk barang tersebut : "))
harga_jual = float(input("\nMasukkan harga jual untuk barang tersebut : "))

print("\nStok Gudang Rincian Barang")
print("###########################")
print("\nNama Barang   :", nama_barang)
print("Jumlah Barang :", jumlah_barang)
print("Harga Beli    : Rp. ", "{:.2f}".format(harga_beli))
print("Harga Jual    : Rp. ", "{:.2f}".format(harga_jual))