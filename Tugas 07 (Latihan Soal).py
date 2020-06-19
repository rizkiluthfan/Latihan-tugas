# TUGAS 7

# Soal 1

p0 = 1000
percent = 0.02
aug = 50
p = 1200

def nbYear(p0, percent, aug, p) :
    
    year = 0
    
    while p0 < p :
        p0 = p0 + (p0 * percent) + aug
        year = year+1
    return year

print(nbYear(p0, percent, aug, p))

# Soal 2
  
def tickets(peopleInLine):
    
    val100 = 100
    val50 = 50
    val25 = 25

    cashier = {val100:0, val50:0, val25:0}

    for cash in peopleInLine:
        if cash == 25:
            cashier[val25] += 1
    
        elif cash == 50:
            if cashier[val25] == 0:
                return 'NO. Vasya will not have enough money to give change to {} dollars' .format(cash)
            cashier[val50] += 1
            cashier[val25] -= 1

        else:
            cashier[val100] += 1
            if cashier[val50] >= 1 and cashier[val25] >= 1:
                cashier[val50] -= 1
                cashier[val25] -= 1

            elif cashier[val25] >= 3:
                cashier[val25] -= 3

            else:
                return 'NO. Vasya will not have enough money to give change to {} dollars' .format(cash)

    return 'YES'
print(tickets([25,25,50,100,50]))

# Soal 3

def rowSumOddNumbers(n):

    num = 1
    for i in range (1, n + 1):
        for j in range (i,i*2):

            print(num, end = ' ')
            num = num+2
        print()

rowSumOddNumbers(2)
