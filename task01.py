import random

a = random.randint(1, 20)

b = int(input('Son kiriting: '))

while a != b:
    if a < b:
        print("Kichik son kiriting!")
    elif a > b:
        print("Katta son kiriting!")
    
    b = int(input('Yana urinib ko‘ring: '))

print("To‘g‘ri topdingiz! ")

    
    

