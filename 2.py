text = input()

cnt = 1
max_cnt = 1

for i in range(1,len(text)):
    if text[i] == text[i-1]:
        cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    else:
        cnt = 1

print(max_cnt)
