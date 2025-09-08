son1 = float(input("1-sonni kiriting: "))
son2 = float(input("2-sonni kiriting: "))
amal = input("Amal: ")

while True:
    if amal == "+":
        print(son1+son2)

    elif amal == '-':
        print(son1-son2)

    elif amal == '*':
        print(son1*son2)

    elif amal == '/':
        print(son1/son2)

    javob = input("Davom etasizmi? (ha/yo'q): ")

    if javob.lower() == "yo'q":
        print("Dastur tugadi: ")
        break
    elif javob.lower() == "ha":
     son1 = float(input("1-sonni kiriting: "))
     son2 = float(input("2-sonni kiriting: "))
     amal = input("Amal: ")


    

