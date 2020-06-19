# TUGAS LIST

# Daftar Pilihan Menu

menu = []

def isi_list(menu):
    isi_list1 = (int(input('Masukkan Banyaknya List : ')))
    for i in range(isi_list1):
        isi_list2 = (int(input('Masukkan Angka : ')))
        menu.append(isi_list2)

def lihat_list(menu):
    print(menu)

def sort_ascend(menu):
    print(sorted(menu))

def sort_descend(menu):
    print(sorted(menu, reverse = True))

def jumlah_maxmin(menu):
    jumlah_max = max(menu)
    jumlah_min= min(menu)
    print('Nilai tertinggi = {}, Nilai terendah = {}'.format(jumlah_max,jumlah_min))

def jumlah_even_odd(menu):
    jumlah_even, jumlah_odd = 0, 0
    for i in menu :
        if i %2 == 0 :
            jumlah_even += 1
        else : 
            jumlah_odd +=1
    print('Jumlah Genap = {}, Jumlah Ganjil = {}'.format(jumlah_even,jumlah_odd))

def exit(menu):
    print('Terimakasih')

#  Tampilan Menu

def submenu(menu) :

    print("MAIN MENU")
    print("")
    print('1. Isi List')
    print('2. Lihat List')
    print('3. Sort List Ascending')
    print('4. Sort List Descending')
    print('5. Nilai Tertinggi dan Terendah')
    print('6. Jumlah Ganjil dan Genap')
    print("7. Keluar")
    pilihan = int(input("Masukkan Pilihan : "))

    if pilihan == 1 :
        isi_list(menu)
        submenu(menu)
    
    elif pilihan == 2 :
        lihat_list(menu)
        submenu(menu)
    
    elif pilihan == 3 :
        sort_ascend(menu)
        submenu(menu)
    
    elif pilihan == 4 :
        sort_descend(menu)
        submenu(menu)
    
    elif pilihan ==5 :
        jumlah_maxmin(menu)
        submenu(menu)
        
    elif pilihan == 6 :
        jumlah_even_odd(menu)
        submenu(menu)
        
    elif pilihan ==7 :
        print('Terimakasih')
    
    else : 
        print('Invalid Input')
        submenu(menu)
        
submenu(menu)
