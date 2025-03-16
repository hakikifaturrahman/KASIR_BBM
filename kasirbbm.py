import datetime

def kasir_bbm():
    harga_bbm = {
        "1": ("PERTALITE", 10000, 1),
        "2": ("PERTAMAX", 12500, 2),
        "3": ("SOLAR", 6800, 3),
        "4": ("PERTAMAX TURBO", 15000, 4),
        "5": ("PERTAMINA DEX", 35090, 5),
    }
    
    print("|-------------------------------------|")
    print("|        Daftar Harga BBM             |")
    print("|-------------------------------------|")
    print("| 1. Pertalite      (Rp 10.000/liter) |")
    print("| 2. Pertamax       (Rp 12.500/liter) |")
    print("| 3. Solar          (Rp  6.800/liter) |")
    print("| 4. Pertamax Turbo (Rp 15.000/liter) |")
    print("| 5. Pertamina Dex  (Rp 35.090/liter) |")
    print("|-------------------------------------|")
    
    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")
    if pilihan not in harga_bbm:
        print("Pilihan tidak valid.")
        return
    
    jenis_bbm, harga_per_liter, pompa = harga_bbm[pilihan]
    
    uang_pembelian = float(input("Masukkan jumlah uang untuk pembelian BBM (dalam ribuan): ")) * 1000
    jumlah_liter = uang_pembelian / harga_per_liter
    
    uang_pembeli = float(input("Masukkan jumlah uang yang diberikan pembeli (dalam ribuan): ")) * 1000
    kembalian = uang_pembeli - uang_pembelian
    
    jumlah_liter_str = f"{jumlah_liter:.2f}"
    waktu_transaksi = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    # Input operator, nomor plat, nomor transaksi, dan shift dari user
    operator = input("Masukkan nama operator: ")
    no_plat = input("Masukkan nomor plat kendaraan: ")
    no_trans = input("Masukkan nomor transaksi: ")
    shift = input("Masukkan shift kerja: ")

    # Menampilkan struk pembelian
    print("\n               PERTAMINA                   ")
    print("             SPBU Hakiki SA                ")
    print(" JL. KESEHATAN NO.10 SUMATERA SELATAN   ")
    print(f" Shift :{shift}  No Trans: {no_trans:<10} ")
    print(f" Waktu :{waktu_transaksi}      ")
    print("---------------------------------------------")
    print(f"Pulau/Pompa : {pompa:<25} ")
    print(f"Nama Produk : {jenis_bbm:<25} ")
    print(f"Harga/Liter : Rp.{harga_per_liter:>10,.3f}")
    print(f"Volume (L)  : {jumlah_liter_str:>3}")
    print(f"Total Harga : Rp.{uang_pembelian:>10,.3f}")
    print(f"Operator    : {operator:<25}")
    print("---------------------------------------------")
    print(f"CASH        : Rp.{uang_pembeli:>10,.3f}")
    print(f"Kembalian   : Rp.{kembalian:>10,.3f}")
    print("---------------------------------------------")
    print(f"No. Plat    : {no_plat:<25}")
    print("---------------------------------------------")
    print("TERIMA KASIH DAN SELAMAT JALAN       ")
    print("SEMOGA SELAMAT SAMPAI TUJUAN          ")
    print("PREMIUM ADALAH BBM BERSUBSIDI           ")
    print("HANYA UNTUK GOLONGAN TIDAK MAMPU        ")
    print("---------------------------------------------")

kasir_bbm()
