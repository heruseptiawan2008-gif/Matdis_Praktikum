naik_motor = True
naik_mobil = True
# XOR: True jika salah satu saja yang True
pilih_satu = naik_motor ^ naik_mobil
if pilih_satu:
    print("Transportasi Valid")
else:
    print("Transportasi Tidak Valid")