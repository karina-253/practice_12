s = input()
w = s.split()

for i in range(len(w)):
    if w.count(w[i]) == 2:
        print(w[i])
        break
        
