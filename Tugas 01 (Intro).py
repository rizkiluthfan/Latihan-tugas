# Soal 1

x = 4
y = 3
z = 2

w = ((x+y*z)/(x*y))**2
print(w)

## Jadi, nilai w = 0.6944444444444445

# Soal 2

angka = int(input("Silahkan masukkan angka berapapun : "))
print("kuadrat dari " + str(angka) + "=" + str(angka ** 2))

# Soal 3

total_hari = int(input("masukkan hari : "))

tahun = str(math.floor(total_hari / 360))
bulan = str(math.floor(total_hari % 360)) / 30)
minggu = str(math.floor(total_hari % 360) %30) /7)
sisahari = str(math.floor(total_hari % 360) %30) %7)

total_hari = (str(tahun) + 'Tahun ' + str(bulan) + 'Bulan ' + str(minggu) + 'Minggu ' + str(sisahari) + 'Hari' )

print(total_hari)

## Jadi 485 hari setara dengan 1 Tahun 4 Bulan 0 Minggu 5 Hari

# Soal 4

total = int(input('Total umur andi dan budi : '))
rasio = float(input('Rasio umur andi dan budi : '))

umur_budi = (total * 10) / (10 + (rasio * 10)) 
umur_andi = total - umur_budi

usia_andi2 = usia_andi + 2 
usia_budi2 = usia_budi + 2

print(usia_andi2)
print(usia_budi2)

# Usia Andi 2 thn kemudian = 16 thn, Usia Budi 2 thn kemudian = 37 thn

# Soal 5

word = input('Kata :')
cari = input('Karakter yang ingin di cari : ')

print(int(len(word.split(cari)))-1)

#Soal 6



#Soal 7 

a = int(input('Masukkan angka : '))

print(a % 100 * 100 + a // 100)

#Soal 8 

from math import pi
r = float(input('Input the radius of the circle :'))
print('The area of the circle is : ' +str(pi * r **2))

#Soal 9 



#Soal 10

a = input('Masukkan kata : ') 
rep = input('Masukkan kata yang ingin di hilangkan : ')
print(a.replace(rep, ' '))

#Soal 11

a = input('Masukkan kata : ')
lis = a.split
print(lis)
print(lis[1] + ' ' + lis[0])
