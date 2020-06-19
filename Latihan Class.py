class BikinMenu ():

    def __init__(self, name, menu, price):
        self.name = name
        self.menu = menu
        self.price = price
        self.history = []
    
    def get_menu(self):

        print('Menu Makanan')
        print('')
        print('{} harganya adalah {}' .format(self.menu[0], self.price[0]))
        print('{} harganya adalah {}' .format(self.menu[1], self.price[1]))
        print('{} harganya adalah {}' .format(self.menu[2], self.price[2]))

    def menu_price(self):
        print('1. {} harganya adalah {}' .format(self.menu[0], self.price[0]))
        print('2. {} harganya adalah {}' .format(self.menu[1], self.price[1]))
        print('3. {} harganya adalah {}' .format(self.menu[2], self.price[2]))
        pilihan = int(input('Pilihan : '))

        if pilihan == 1:
            print('{} telah membeli {} dengan harga {}' .format(self.name, self.menu[0], self.price[0]))
        
        elif pilihan == 2:
            print('{} telah membeli {} dengan harga {}' .format(self.name, self.menu[1], self.price[1]))

        elif pilihan ==3:
            print('{} telah membeli {} dengan harga {}' .format(self.name, self.menu[2], self.price[2]))
        
        else :
            print('Invalid')
            return 
    
Paul = BikinMenu('Paul', ['Ayam Goreng', 'Nasi Bakar', 'Sate Kambing'], [1000, 2000, 3000])

Paul.get_menu()
Paul.menu_price()