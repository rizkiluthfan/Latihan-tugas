# Write an algorithm that takes a list and moves all the zeros to the end of the list,
# preserving the order of the other elements

# moveZeros([False, 1,0,1,2,0,1,3,"a"])
# moveZeros([0,0,0,"Test", 0,3,"a", True])
# moveZeros([True, True, False, "a", "b", 1,1,1])


# def moveZeros(num):
#     result = []

#     for index, digit in enumerate(str(num)[::-1]):
#         if int(digit) != 0:
#             result.append(digit + ('0' * index))

#     return ' + '.join(result[::-1])

# moveZeros([False, 1,0,1,2,0,1,3,"a"])
# moveZeros([0,0,0,"Test", 0,3,"a", True])
# moveZeros([True, True, False, "a", "b", 1,1,1])

def moveZeros(list):
    
    new = []
    zero = []
    
    for i in range(len(list)):
        if list[i] == 0 :
            if type(list[i]) == False :
                zero.append(list[i])
            else: new.append(list[i])
        else:
            new.append(list[i])
    
    return new + zero
    
print(moveZeros([False, 1,0,1,2,0,1,3,"a"]))
print(moveZeros([0,0,0,"Test", 0,3,"a", True]))
print(moveZeros([True, True, False, "a", "b", 1,1,1]))

# Write a function that takes in a string of one or more words, and returns the same string, 
# but if the word have 5 or more letter, the word would be reversed. Strings passed in will consist
# of only letters and spaces. Spaces will be included only ehwn more than one word presentdatetime A combination of a date and a time. Attributes: ()

# spinWords('Hey fellow warriors')
# spinWords('This is a test')
# spinWords('This is another test')


def spinWords(sentence):
    
    word = sentence.split()
    spin = []

    for i in word:
        if len(i) >= 5:
            spin.append(i[::-1])
        else:
            spin.append(i)
            
    return ' '.join(spin)

print(spinWords('Hey fellow warriors'))
print(spinWords('This is a test'))
print(spinWords('This is another test'))
