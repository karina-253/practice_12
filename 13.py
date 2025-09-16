cnt = 0

while True:
    n = input()
    cnt += 1

    if len(n) % 2 == 0:
        h1 = n[:len(n) // 2]
        h2 = n[len(n) // 2:]
        if sum(map(int, h1)) == sum(map(int, h2)):
            print(cnt)
            break
