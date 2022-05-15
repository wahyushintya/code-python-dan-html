print("~~~~~~~~")
pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 

def kasir():
    # masukan input dari user
    nama_barang = input('masukan pesanan anda: ')
    harga = int(input('masukan harga barang: '))
    jumlah_beli = int(input('masukan jumlah barang yang anda beli: '))
 
    # mengitung jumlah harga
    total = harga * jumlah_beli
     
    # cetak total harga
    print(f'harga total: {nama_barang}, = {total}')
 
    # input pembayaran dari user
    bayar = int(input('masukan pembayaran: '))
 
    # mengecek apakah pembayaran kurang atau ada kembalian
    kurang = total - bayar
    kembalian = bayar - total
 
    if bayar > total:
        print(f'jumlah kembalian anda adalah {kembalian}')
        tanya()
     
    elif bayar == total:
        print('uang anda pas, terimakasih telah berbelanja ')
 
    else:
        print(f'maaf uang anda tidak cukup, uang anda kurang {kurang}')
        counter_kasir()
