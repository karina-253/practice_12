city = input()
w = city.split()

def e2(x):
    ch = x[-1].lower()
    if ch in ['ь', 'ъ', 'ы', 'й']:
        return x[-2].lower()
    return ch

for i in range(1, len(w)):
    if e2(w[i-1]) != w[i][0].lower():
        if i % 2 == 1:
            print('Петя нарушил правила игры')
        else:
            print('Вася нарушил правила игры')
        break

if len(w) % 2 == 0:
    print('Вася выиграл')
else:
    print('Петя выиграл')
