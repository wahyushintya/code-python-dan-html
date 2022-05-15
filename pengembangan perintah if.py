print('Program menghitung luas, volume, dan keliling balok')
p = int(input('masukan panjang balok: '))
l = int(input('masukan lebar balok: '))
t = int(input('masukan tinggi balok: '))
 
def luas_permukaan(p,l,t):
    L = 2 * ( (p*l) + (p*t) + (l*t) )
    return L
 
def volume(p,l,t):
    V = p * l * t
    return V
 
def keliling(p,l,t):
    k = 4 * (p + l + t)
    return k
 
 
print('Jadi balok dengan ukuran panjang:{}, lebar:{}, tinggi:{} \nMempunyai luas:{} , volume:{} , keliling:{}'.format(p,l,t, luas_permukaan(p,l,t), volume(p,l,t), keliling(p,l,t)))

#Penjelasan:
#1- kita membuat variable inputan p, l, dan t terlebih dahulu,
#2- selanjutkan membuat masing-masing fungsi dari rumus luas, volume, dan keliling
#3- Cetak hasilnya

#Dalam code diatas, setelah mendapat input p, l, t , program langsung menghitung luas, volume, dan keliling balok. Gimana kalau kita kreasikan menjadi pilihan? misal kita ingin menghitung volume saja, atau luas saja? terserah pilihan kita?.

print('Program menghitung\n1. luas,\n2. volume\n3. keliling balok')
pilihan = int(input('Masukan pilihan: '))
 
def luas_permukaan(p,l,t):
    L = 2 * ( (p*l) + (p*t) + (l*t) )
    return L
 
def volume(p,l,t):
    V = p * l * t
    return V
 
def keliling(p,l,t):
    k = 4 * (p + l + t)
    return k
 
if pilihan == 1:
    p = int(input('masukan panjang balok: '))
    l = int(input('masukan lebar balok: '))
    t = int(input('masukan tinggi balok: '))
    luas_permukaan(p,l,t)
    print('Jadi balok dengan ukuran panjang:{}, lebar:{}, tinggi:{}\nMempunyai luas:{}'.format(p,l,t, luas_permukaan(p,l,t)))
 
elif pilihan == 2:
    p = int(input('masukan panjang balok: '))
    l = int(input('masukan lebar balok: '))
    t = int(input('masukan tinggi balok: '))
    volume(p,l,t)
    print('Jadi balok dengan ukuran panjang:{}, lebar:{}, tinggi:{}\nMempunyai volume:{}'.format(p,l,t, volume(p,l,t)))
 
elif pilihan == 3:
    p = int(input('masukan panjang balok: '))
    l = int(input('masukan lebar balok: '))
    t = int(input('masukan tinggi balok: '))
    keliling(p,l,t)
    print('Jadi balok dengan ukuran panjang:{}, lebar:{}, tinggi:{}\nMempunyai keliling:{}'.format(p,l,t, keliling(p,l,t)))
 
else:
    print('Pilihan tidak tersedia')
