n = int(input("Введите число: "))

f = {1 : 'один', 2 : 'два', 3 : 'три', 4 : 'четыре', 5 : 'пять', 6 : 'шесть', 7 : 'семь', 8 : 'восемь', 9 : 'девять'}
l = {10 : 'десять', 20 : 'двадцать', 30 : 'тридцать', 40 : 'сорок', 50 : 'пятьдесят', 60 : 'шестьдесят', 70 : 'семьдесят', 80 : 'восемьдесят', 90 : 'девяносто'}
k = {100 : 'сто', 200 : 'двести', 300 : 'триста', 400 : 'четыреста', 500 : 'пятьсот', 600 : 'шестьсот', 700 : 'семьсот', 800 : 'восемьсот', 900 : 'девятьсот', 1000 : 'тысяча'}
s = {11 : 'одиннадцать', 12 : 'двенадцать', 13 : 'тринадцать', 14 : 'четырнадцать', 15 : 'пятнадцать', 16 : 'шестнадцать', 17 : 'семнадцать', 18 : 'восемнадцать', 19 : 'девятнадцать'}

if len(str(n)) == 1:
    print(f.get(n))

elif len(str(n)) == 2:
    if n >= 10 and n < 20:
        print(s.get(n))
    elif n >= 20 and n < 100:
        print(l.get(n//10 * 10), end = ' ')
        print(f.get(n%10))

elif len(str(n)) == 3:
    print(k.get(n // 100 * 100), end=' ')
    if n%100 >= 10 and n%100 < 20:
        print(s.get(n%100))
    elif n%100 >= 20 and n%100 < 100:
        print(l.get(n%100//10*10), end = ' ')
        print(f.get(n%10))

elif len(str(n)) == 4:
    print(k.get(n))