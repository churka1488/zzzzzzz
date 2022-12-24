import math 
def info():
    dano = 0
    dano = int(input("Выберите, что нужно найти: \n1) N - мощность алфавита \n2) k - количество символов \n3) I - информационный объем текста \n4) i - информационнй объем одного символа \nВыбор: "))
    if dano != 4: cond = str(input("Дано ли i? (введите yes/no):"))
    if dano == 1:
        if cond == 'no':
            I = int(input("Ввидите в битах. I="))
            k = int(input("k="))
            print(f"N = {2**(I/k)}")
        else:
            i = int(input("Ввидите в битах. i="))
            print(f"N = {2**i}")

    if dano == 2:
        if cond == 'no':
            N = int(input("N="))
            I = int(input("Ввидите в битах. I="))
            print(f"k = {I/math.log2(N)}")
        else:
            i = int(input("Ввидите в битах. i="))
            I = int(input("Ввидите в битах. I="))
            print(f"k = {I/i}")
    if dano == 3:
        if cond == 'no':
            N = int(input("N="))
            k = int(input("k="))
            print(f"I = {math.log2(N)*k}")
        else:
            i = int(input("Ввидите в битах. i="))
            k = int(input("k="))
            print(f"I = {i*k}")
    if dano == 4:
        condi = str(input("Дано ли N? (введите yes/no):"))
        if condi == 'no':
            N = int(input("N="))
            print(f"i = {math.log2(N)}")
        else:
            I = int(input("Ввидите в битах. I="))
            k = int(input("k="))
            print(f"i = {I/k}")






def sound():
    dano = 0
    # yslov = int(input("Выбирите тип аудиофайла:\n1) моноаудиофайл\n2) стериоаудио файл\nВыбор: "))
    # if yslov == 1:
    #     koo = 1 
    # if yslov == 2:
    #     koo = 2 
    dano = int(input("Выберите, что найти: \n1) A - размер цифрового аудиофайла\n2) D - частота дискритизации\n3) Т - время звучания\n4) I - разрядность регистора\nВыбор: "))   
    if dano == 1:
        D = int(input("Ввидите в Гц. D(частота дискритизации) = "))
        T = int(input("Т(время звучания) = "))
        I = int(input("I(разрядность регистора) = "))
        A = D*T*I
        print(A)
    if dano == 2:
        A = int(input("Ввидите в битах. A(размер цифрового аудиофайла) = "))
        T = int(input("Т(время звучания) = "))
        I = int(input("I(разрядность регистора) = "))
        D = A/T/I
        print(D)
    if dano == 3:
        A = int(input("Ввидите в битах. A(размер цифрового аудиофайла) = "))
        I = int(input("I(разрядность регистора) = "))
        D = int(input("Ввидите в Гц. D(частота дискритизации) = "))
        T = A/D/I
        print(f"T = {A/D/I}")
    if dano == 4:
        D = int(input("Ввидите в Гц. D(частота дискритизации) = "))
        T = int(input("Т(время звучания) = "))
        A = int(input("Ввидите в битах. A(размер цифрового аудиофайла) = "))
        print(f"I = {A/D/T}")

def pic():
    dano = int(input("Выберите, что найти: \n1) k - количество цветов в палитре \n2) I - глубина цвета или битовая глубина"))
    if dano == 1:
        I = int(input("I = "))
        print(f"I =  {math.log2(k)}")               
    if dano == 2:
        k = int(input("k = "))
        print(f"I =  {2**k}")

zadacha = int(input("Выберите тип задачи: \n1) задачи на кодирование информации \n2) задачи на кодирование звука \n3) задачи на кодирование изображение\nВыбор: "))
if zadacha == 1:
        info()
if zadacha == 2:
        sound()
if zadacha == 3:
        pic()
