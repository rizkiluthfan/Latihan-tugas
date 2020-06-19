def fungsi(x):
    return 0

def fungsi2(x,y):
    return 0

def fungsi3(z):
    return[0]

def fungsi4():
    return 0

Contoh = [{'Test_1': [{0: print('Berhasil')}]}] #key = 0
z = 0
x = 0
y = 17971979

Contoh[fungsi(x)]['Test_1'][fungsi2(x,y)][fungsi3(z)[fungsi4()]]

def get_highest_xnum(num, sequence):
    
    newlist = [] # bikin newlist, newlist akan di isi list
    hasil = '' # bikin hasil, hasil di jadikan string 

    for angka in str(num) : # num di jadikan string
        newlist.append(int(angka)) # append angka ke list

    index = newlist.index(max(newlist)) # cari angka terbesar dari index
    for angka_baru in newlist[index : index + sequence]:
        hasil = hasil + str(angka_baru)

    print('The highest {}-number is {}' .format(sequence, hasil))

get_highest_xnum(679988789, 5)