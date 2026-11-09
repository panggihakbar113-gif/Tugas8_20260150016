from modul_sensor import (LOKASI,AMBANG_KRITIS,hitung_tren,evaluasi_irigasi)

# List untuk menyimpan data sensor
log_kebun = []

# Fungsi validasi input sensor
def input_sensor():
    while True:
        try:
            suhu = float(input("Masukkan suhu udara (0-100 C): "))
            kelembaban = float(input("Masukkan kelembaban tanah (0-100%): "))

            if not (0 <= suhu <= 100):
                print("Suhu harus berada di antara 0-100!")
                continue

            if not (0 <= kelembaban <= 100):
                print("Kelembaban harus berada di antara 0-100!")
                continue

            return (suhu, kelembaban)

        except ValueError:
            print("Input harus berupa angka! Silakan coba lagi.")


# Program utama
print("========================================")
print(" SISTEM MONITORING IOT KAMPUNG ANGGUR")
print("========================================")
print("Lokasi:", LOKASI[0])
print("Koordinat:", LOKASI[1], ",", LOKASI[2])


while True:
    print("\n========== MENU UTAMA ==========")
    print("[1] Rekam Data Sensor")
    print("[2] Analisis Tren (3 Terakhir)")
    print("[3] Keluar")

    pilihan = input("Pilih menu (1-3): ")

    # Menu 1: Rekam data
    if pilihan == "1":
        data = input_sensor()
        log_kebun.append(data)

        print("\nData sensor berhasil direkam!")
        print("Suhu:", data[0], "C")
        print("Kelembaban:", data[1], "%")

    # Menu 2: Analisis tren
    elif pilihan == "2":

        if len(log_kebun) == 0:
            print("\nBelum ada data sensor!")
            continue

        # Mengambil maksimal 3 data terakhir menggunakan slicing
        data_terakhir = log_kebun[-3:]

        print("\n======= DATA 3 TERAKHIR =======")

        # Menampilkan data menggunakan list iteration
        for i, data in enumerate(data_terakhir, start=1):
            print(f"Data ke-{i}: Suhu {data[0]} C, "
                  f"Kelembaban {data[1]} %")

        # Menghitung rata-rata menggunakan fungsi modul
        rata_suhu, rata_lembab = hitung_tren(data_terakhir)

        print("\n======= HASIL ANALISIS =======")
        print(f"Rata-rata Suhu: {rata_suhu:.2f} C")
        print(f"Rata-rata Kelembaban: {rata_lembab:.2f} %")

        # Mengevaluasi kondisi irigasi
        status = evaluasi_irigasi(rata_suhu,rata_lembab,AMBANG_KRITIS)

        print("Status Irigasi:", status)

    # Menu 3: Keluar
    elif pilihan == "3":
        print("\nTerima kasih telah menggunakan sistem monitoring!")
        break

    else:
        print("\nPilihan tidak valid! Silakan pilih 1-3.")
