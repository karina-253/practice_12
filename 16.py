text = input()
cnt = 0

for ch in text:
    if ch == '(':
        cnt += 1
    elif ch == ')':
        cnt -= 1
        if cnt < 0:
            print('лишняя скобка справа')
            exit()
            
if cnt == 0:
    print('верно')
else:
    print('неверно')
    
