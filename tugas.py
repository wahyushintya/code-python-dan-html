print("Program menghitung luas, volume,dan keliling balok")
p = int(input("Masukan panjang balok: "))
l = int(input("Masukan lebar balok: "))
t = int(input("Masukan tinggi balok:"))

def luas_permukaan(p,l,t):
    L=2*( (p*l)+(p*t)+(l*t) )
    return L

def volume(p,l,t):
    V=p*l*t
    return V

def keliling(p,l,t):
    K=4*(p+l+t)
    return K

print("Jadi balok depan dengan ukuran panjang:{},lebar:{},tinggi:{} \nMempunyai luas:{},volume:{},keliling:{}".format(p,l,t,luas_permukaan(p,l,t),volume(p,l,t),keliling(p,l,t)))


print("Program menghitung\n1.luas,\n2.volume\n3.keliling balok")
pilihan = int(input("Masukan Pilihan: "))

def luas_permukaan(p,l,t):
    L =2*( ( p*l) +(p*t)+(l*t) )
    return L
def volume(p,l,t):
    V =p*l*t
    return V
def keliling(p,l,t):
    K=4*(p+l+t)
    return K

if pilihan ==1:
    p = int(input("Masukan panjang balok: "))
    l = int(input("Masukan lebar balok: "))
    t = int(input("Masukan tinggi balok: "))
    print("Jadi balok dengan ukuran panjang:{},lebar:{},tinggi:{}\nMempunyai luas:{}".format(p,l,t,luas_permukaan(p,l,t)))

elif pilihan ==2:
    p = int(input("Masukan panjang balok: "))
    l = int(input("Masukan lebar balok: "))
    t = int(input("Masukan tinggi balok: "))
    print("Jadi balok dengan ukuran panjang:{},lebar:{},tinggi:{}\nMempunyai volume:{}".format(p,l,t,volume(p,l,t)))

elif pilihan ==3:
    p = int(input("Masukan panjang balok: "))
    l = int(input("Masukan lebar balok: "))
    t = int(input("Masukan tinggi balok: "))
    print("Jadi balok dengan ukuran panjang:{},lebar:{},tinggi:{}\nMempunyai keliling:{}".format(p,l,t,keliling(p,l,t)))

else:
    print("Pilihan tidak tersedia")





