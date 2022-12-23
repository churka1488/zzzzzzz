def noten():
    N10 = int(input('Введите исходное 10-тичное число: '))
    p = 1
    while ((p < 2) or (p > 9)):
        p = int(input('Введите основание системы счисления в диапазоне [2; 9]: '))
    k = int(1)
    Np = int(0)
    while not (N10 == 0):
        Np = Np + (N10 % p) * k
        k = k * 10
        N10 = N10 // p
    print('N' + str(p) + ' = ' + str(Np))

def ten():
    p = int(input('Введите основание СС исходного числа: p = '))
    valid = False
    while valid == False:
        Np = (input(f'Введите исходное число: N{p} = '))
        for i in range(1, len(Np)):
            if int(Np[i]) >= p:
                print('Недопустимое число!')
                valid = False
                break
            else:
                valid = True
                Np = int(Np)
    k = int(1)
    N10 = int(0)
    while not Np == 0:
        N10 = N10 + (Np % 10) * k
        k = k * p
        Np = Np // 10
    print(f'N10 = {N10}')

def operation():
    print("введите p (2 < p <= 10): ")
    p = int(input())
    for X in range(1, p - 1):
        for Y in range(1, p - 1):
            Z = (X * X / p) * 10 + (X * Y % p)
            print(f'{Z:03}')
        print("\n")
        return
    return

def distance(x, y):
    k = 7
    for i in range(7):
        if x % 10 == y % 10:
            k = k - 1
        x = x // 10
        y = y // 10
    return k

def hemming():
    a = '0123456789'
    nums = list(a)
    print(nums)

    ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    b = '0000000 000111 0010110 0011001 0100101 0101010 0110011 0111100 1000011 1001100'
    hem = b.split()
    print(hem)
    for i in range(len(hem)):
        hem[i] = int(hem[i])
    print(hem)

    cod = int(input("код="))

    min = distance(cod, hem[0])
    imin = 0
    for i in range(10):
        D = distance(cod, hem[i])
        if D:
            min = D
            imin = i
    if min == 0:
        print(f"Код верный: символ {nums[imin]}")
    elif min == 1:
        print(f"Код исправлен: символ {nums[imin]}")
    else:
        print(f"Код неверный")

def morze():
    A = list('АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
    a = list('абвгдежзийклмнопрстуфхцчшщъыьэюя')
    Morze = list(
        [".-", "-...", ".--", "--.", "-..", ".", "...-", "--..", "..", ".---", "-.-", ".-..", "--", "-", "---", ".--.",
         ".-.", "...", "-", "..-", "..-.", "....", "-.-.", "---.", "----", "--.-", ".--.-", "-.--", "-..-", "..-..",
         "..--", ".-.-"])
    InpS = input('Введите исходную строку: ')
    OutS = str('')
    for i in range(1, (len(InpS) + 1)):
        for j in range(1, 32):
            if (InpS[i - 1] == str(A[j - 1])) or (InpS[i - 1] == str(a[j - 1])):
                OutS = OutS + str(Morze[j - 1]) + ' '
    print('Ваша строка, перекодированная на азбуку Морзе: ' + OutS)

def menu():
    start = True
    print(
        'Выберите нужную функцию\n1 - перевод числа из 10-чной в N-ю \n2 - перевод числа из N-й в 10-ю\n3 - код хемминга\n4 - слово на азбуке морзе\n5 - умножение чисел в различных системах счисления')
    while (start):
        arg = int(input())
        match arg:
            case 1:
                noten()
                break
            case 2:
                ten()
                break
            case 3:
                hemming()
                break
            case 4:
                morze()
                break
            case 5:
                operation()
                break
        print('хотите еще? 1 - да, 0 - нет')
        ans = int(input())
        if ans:
            start = True
        else:
            start = False
    return

if __name__ == '__main__':
    menu()
