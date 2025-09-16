text = input()

cnt = 0
max_cnt = 0

for ch in text:
    if ch == ' ':
        cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    else:
        cnt = 0

print(max_cnt)
