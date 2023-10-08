str = input("Введите строку: ")

i = 0
while i < len(str):
    k = 1
    j = i
    while j + 1 < len(str):
        if str[j + 1] == str[j]:
            j += 1
            k += 1
        else:
            break
    print(str[i], end = '')

    if k > 1:
        print(k, end = '')
    i += k
