s = input()
w = s.split()

for i in w:
    if i != w[0] and len(i) == len(set(i)):
        print(i)
        
