punya_kartu = False 
punya_e_wallet = True 

bayar = punya_kartu or punya_e_wallet 

if bayar:
	print("Pembayaran Berhasil")
else:
	print("Pembayaran Gagal")
