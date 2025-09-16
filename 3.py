text = input()
let = []

for ch in text:
    if ch not in let:
        let.append(ch)

print(len(let))
