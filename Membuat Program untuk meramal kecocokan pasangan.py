""" Nathan Septian """
""" Membuat Program untuk meramal kecocokan pasangan """
import random


def kecocokan_pasangan():
    print("Selamat Datang di program Ramalan Cupu")
    print("++++++++++++++++++++++++++++++++++++++")
    # Masukan nama dan umur kamu
    print("\nData Anda:")
    print("♥♥♥♥♥♥♥♥♥♥♥")
    nama_user = input("Masukkan nama Anda: ")
    umur_user = int(input("Masukkan umur Anda: "))

    # Masukkan nama dan umur pasangan
    print("")
    print("Data Pasangan Anda:")
    print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
    nama_pasangan = input("Masukkan nama pasangan Anda: ")
    umur_pasangan = int(input("Masukkan umur pasangan Anda: "))

    # Menampilkan nama dan umur kamu serta pasangan kamu
    print("\n",nama_user ,"[", umur_user ,"] ","tahun")
    print()
    print()
    print("   ♥♥♥   ♥♥♥")
    print("  ♥♥♥♥♥  ♥♥♥♥♥")
    print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
    print(" ♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
    print("   ♥♥♥♥♥♥♥♥♥♥")
    print("    ♥♥♥♥♥♥♥♥")
    print("      ♥♥♥♥")
    print("       ♥♥      ")
    print()
    print()
    print(nama_pasangan, "[", umur_pasangan ,"] ","tahun")
    print()

    # Hitung kecocokan berdasarkan rumus
    kecocokan = random.randint(50, 100) / 1.1

    # Tampilkan hasil kecocokan antara kamu dan pasangan mu
    print("\nTekan ENTER untuk melihat hasil ramalan...")
    print("\nKecocokan anda dengan pasangan anda adalah :", "{:.2f}".format(kecocokan) ,"%")
    print("\n\nTerima kasih karena anda telah menggunakan jasa ramalan kami.. ^^")

# Panggil fungsi kecocokan_pasangan()
kecocokan_pasangan()