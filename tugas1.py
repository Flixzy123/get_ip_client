
berat_telur = int(input('Masukan Jumlah telur : '))
harga_telur = int(input('Masukan Harga telur per KG : '))
transport = int(input('Tarif Pulang Pergi : '))
uang_ibu = 200000
total_belanja = berat_telur * harga_telur - transport
sisa_uang = uang_ibu - total_belanja

print(f'Sisa Uang Ibu: Rp.{sisa_uang}')
