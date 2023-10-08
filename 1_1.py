str = input("Введите строку: ")

i = 0
while i < len(str):
    if not str[i].isdigit():
        if i+1 < len(str) and str[i+1].isdigit():
            k = 1
            while i + k < len(str) and str[i + k].isdigit():
                k += 1
            a = int(str[i+1: i + k])

            for j in range(0, a):
                print(str[i], end = '')
            i += k
        else:
            print(str[i], end = '')
            i += 1
