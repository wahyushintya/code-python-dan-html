nama = input("Masukan nama anda: ")
tahun = int(input("Masukan Tahun lahir anda: "))

if (tahun >=1944) and (tahun <=1964):
    generasi = "X"
elif (tahun >=1980) and (tahun <=1994):
    generasi = "Y"
elif (tahun >=1995) and (tahun <=2015):
    generasi = "Z"
else:
    generasi = "Tidak tergolong"


print("Anda termasuk golongan generasi", generasi)
