# Konstanta lokasi dan ambang kritis
LOKASI = ("Kampung Anggur Plumbungan", -7.828, 110.378)

AMBANG_KRITIS = (35.0, 40.0)


# menghitung rata-rata suhu dan kelembaban
def hitung_tren(data_slice):
    total_suhu = 0
    total_lembab = 0

    for suhu, kelembaban in data_slice:
        total_suhu += suhu
        total_lembab += kelembaban

    jumlah_data = len(data_slice)

    rata_suhu = total_suhu / jumlah_data
    rata_lembab = total_lembab / jumlah_data

    return rata_suhu, rata_lembab


# evaluasi kondisi irigasi
def evaluasi_irigasi(rata_suhu, rata_lembab, tuple_kritis):
    suhu_max, lembab_min = tuple_kritis

    if rata_suhu > suhu_max or rata_lembab < lembab_min:
        return "KRITIS: Nyalakan Pompa Irigasi!"
    else:
        return "NORMAL: Pompa Mati."
