# TUGAS 

n = int(input('Angka : '))

def triangle ():

    num = 1
    for i in range (1, n + 1):
        for j in range (i,i*2):

            print(num, end = ' ')
            num = num+1
        print()

triangle()
