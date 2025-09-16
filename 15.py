def p7(x):
    if len(x) != 4 or len(set(x)) != 4 or not x.isdigit():
        return False
    return True

number = input()

while not p7(number):
    print('Введите четырехзначное целое число '
          'с неповторяющимися цифрами')
    number = input()

print('\n'*25)

att = 10

while att>0:
    n=input()

    if not p7(n):
        print('Ошибка! Введите корректное число.')
        continue

    bull = 0
    cow = 0

    for i in range(4):
        if n[i] == number[i]:
            bull += 1
        elif n[i] in number:
            cow+=1
    print(f'Быков: {bull} Коров: {cow}')

    if bull == 4:
        print('Победа!')
        break
    else:
        att -= 1

if att == 0:
    print('Проигрыш!')
    print(f'Загаданное число:{number}')
