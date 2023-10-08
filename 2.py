str = input("Введите строку: ")

i = set(str)
count = []
for j in i:
    count.append((str.count(j), j))
count.sort(reverse=True)

for i in range(0, 3):
    print(count[i], end = '')