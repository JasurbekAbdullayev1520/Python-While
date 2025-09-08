s = 0 


while True:
    a = input("+ yoki stop kiriting: ")

    if a == '+':
        s += 10
        print("Ball:", s)

    elif a == 'stop':
        print("O‘yinda to‘plangan ball:", s)
        break

    else:
        print("Faqat '+' yoki 'stop' yozing!")



