ip_dari_internet = True
port_https = False  # Menggunakan HTTP biasa (Port 80)

# Implikasi: p -> q (Sama dengan: not p or q)
traffic_aman = (not ip_dari_internet) or port_https

if traffic_aman:
    print("Paket Data Diizinkan Lewat Firewall")
else:
    print("BLOKIR: Paket dari luar wajib HTTPS!")