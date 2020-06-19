import random

class ramal:
    
    def __init__(self, value):
        self.val = value

    def menu(self):

        def ramal_kerja(value):     

            reading = {
            1: "Masih butuh banyak pengalaman.",
            2: "Lebih baik cari pekerjaan lain.",
            3: "Pekerjaan masih stabil.",
            4: "Keberuntungan menunggu anda.",
            5: "Anda akan sukses dalam pekerjaan."
            }

            prob = []
            
            if value <= 10000:
                for n in range(5):
                    prob.append(random.randint(1,3))
                    
                for n in range(1,3):
                    prob.append(n)
                    
                print('Hasil Ramalan: {}'.format(reading[prob[random.randint(0,5)]]))

            elif value > 10000 or value <=50000 :
                for n in range(5):
                    prob.append(random.randint(2,4))
                prob.append(1)
                prob.append(5)

                print('Hasil Ramalan: {}'.format(reading[prob[random.randint(0,5)]]))  

            elif value > 50000 :
                for n in range(5):
                    prob.append(random.randint(3,5))
                for n in range(4,6):
                    prob.append(n)

                print('Hasil Ramalan: {}'.format(reading[prob[random.randint(0,5)]]))  
        
        def ramal_kesehatan(value):     

            reading = {
            1: "Anda harus segera ke dokter.",
            2: "Kesehatan mulai memburuk.",
            3: "Kesehatan stabil.",
            4: "Kondisi anda cukup baik.",
            5: "Kondisi kesehatan anda sangat baik."
            }

            prob = []
            
            if value <= 10000:
                for n in range(5):
                    prob.append(random.randint(1,3))
                
                for n in range(1,3):
                    prob.append(n)
                    
                print('Hasil Ramalan: {}'.format(reading[prob[random.randint(0,5)]]))

            elif value > 10000 or value <=50000 :
                for n in range(5):
                    prob.append(random.randint(2,4))
                prob.append(1)
                prob.append(5)

                print('Hasil Ramalan: {}'.format(reading[prob[random.randint(0,5)]]))  

            elif value > 50000 :
                for n in range(5):
                    prob.append(random.randint(3,5))
                for n in range(4,6):
                    prob.append(n)
                    
                print('Hasil Ramalan: {}'.format(reading[prob[random.randint(0,5)]]))  
        
        def ramal_cinta(value):     

            reading = {
            1: "Mulai bosan.",
            2: "Menunggu waktu yang tepat.",
            3: "Hubungan masih stabil.",
            4: "Hubungan anda akan berjalan baik.",
            5: "Sangat baik. Pertahankan hubungan anda."
            }
            
            prob = []
            
            if value <= 10000:
                for n in range(5):
                    prob.append(random.randint(1,3))
                
                for n in range(1,3):
                    prob.append(n)
                    
                print('Hasil Ramalan: {}'.format(reading[prob[random.randint(0,5)]]))

            elif value > 10000 or value <=50000 :
                for n in range(5):
                    prob.append(random.randint(2,4))
                prob.append(1)
                prob.append(5)

                print('Hasil Ramalan: {}'.format(reading[prob[random.randint(0,5)]]))  

            elif value > 50000 :
                for n in range(5):
                    prob.append(random.randint(3,5))
                for n in range(4,6):
                    prob.append(n)
                    
                print('Hasil Ramalan: {}'.format(reading[prob[random.randint(0,5)]]))  

        while True :
                
            print('App Ramalan Terkini')
            print('')        
            print('Pilih Ramalan anda: ')
            print('1. Ramalan Pekerjaan')
            print('2. Ramalan Kesehatan')
            print('3. Ramalan Percintaan')
            print('4. Keluar')

            pilihan = int(input('Masukkan Pilihan: '))
            
            if pilihan == 1:
                ramal_kerja(self.val)

            elif pilihan == 2:
                ramal_kesehatan(self.val)

            elif pilihan == 3:
                ramal_cinta(self.val)

            elif pilihan == 4:
                print('Terima Kasih')
                break

            else : 
                print('invalid input')
                return 

Cornell = ramal(50000)
Cornell.menu()

print(random.randint(3,5))
