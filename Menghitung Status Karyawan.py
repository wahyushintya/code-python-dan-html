#penilaian appraisal karyawan berdasarkan persentase kehadiran
Hari = int(input("Masukan Jumlah Hari Kerja= "))
Masuk = int(input("Masukan Jumlah hari Masuk= "))
Absen = Masuk/Hari*100

if (Absen>=80):
    status = "A"
else :
    status = "C"

print ("Nilai kamu adalah", status)
    
