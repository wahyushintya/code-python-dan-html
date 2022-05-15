pilihan="Y"
while pilihan=="Y":
    print("""
   RESTORAN SEHATI
MENU=
   1. NASI GORENG
   2. MIE GORENG
   3. FUYUNG HAI
   4. NASI PUTIH
   5. ES TEH
   6. ES JERUK
   7. ES DALUMAN
   8. ES CAMPUR
    """)
    pesan=str(input("masukkan list menu ="))
    jumlahpesan=int(input("masukkan jumlah pesanan ="))
    if pesan == "1":
        listnama= "NASI GORENG"
        harga=(20000*jumlahpesan)
        ppn= int(harga * 0.15)
        if jumlahpesan >= 3:
            diskon = int(harga*0.1)
            totalharga=int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga=int(harga+ppn)
    elif pesan == "2":
        listnama= "MIE GORENG"
        harga = (20000*jumlahpesan)
        ppn = int(harga * 0.15)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga =int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga =int(harga+ppn)
    elif pesan == "3":
        listnama= "FUYUNG HAI"
        harga=int(15000*jumlahpesan)
        ppn = int(harga * 0.15)
        diskon=0
        totalharga=int(harga+ppn)
    elif pesan == "4":
        listnama= "NASI PUTIH"
        harga=int(10000*jumlahpesan)
        ppn = int(harga * 0.15)
        diskon=0
        totalharga = int(harga+ppn)
    elif pesan == "5":
        listnama= "ES TEH"
        harga=int(7000*jumlahpesan)
        ppn = int(harga * 0.15)
        diskon=0
        totalharga = int(harga+ppn)
    elif pesan == "6":
        listnama= "ES JERUK"
        harga=int(8000*jumlahpesan)
        ppn = int(harga * 0.15)
        diskon=0
        totalharga = int(harga+ppn)
    elif pesan == "7":
        listnama= "ES DALUMAN"
        harga=int(15000*jumlahpesan)
        ppn = int(harga * 0.15)
        diskon=0
        totalharga = int(harga+ppn)
    elif pesan == "8":
        listnama= "ES CAMPUR"
        harga=int(15000*jumlahpesan)
        ppn = int(harga * 0.15)
        diskon=0
        totalharga = int(harga+ppn)
    else:
        pilihan=input("menu tidak tersedia, silahkan masukkan abjad menu yang tersedia silahkan ulangi kembali Y/N =")
 

    print()
    print("PEMBAYARAN")
    print("Menu :",listnama)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga :", harga)
    print("Diskon :", diskon)
    print("PPN :", ppn)
    print("Jumlah Bayar :", totalharga)
    pilihan=input("apakah anda ingin order kembali Y/N =")
