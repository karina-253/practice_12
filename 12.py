import keyword

s = input()

if s[0] in '1234567890':
    print('Неверное имя')
    exit()
    
if keyword.iskeyword(s):
    print('Неверное имя')
    exit()
    
for ch in s:
    if ch not in ('1234567890_qwertyuiopasdfghjklzxcvbnm'
                  'QWERTYUIOPASDFGHJKLZXCVBNM'):
        print('Неверное имя')
        break
else:
    print('Верное имя')
    
