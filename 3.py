import csv
with open("C:\\Users\\Kids01\\Desktop\\Вариант 18\\languages.csv",
          encoding='utf8') as r:
    s = csv.reader(r, delimiter=';', quotechar='"')
    s = list(s)
    del s[0]
    while True:
        a = input()  # запрос на введение названия ЯП
        if a == '0':
            break
        f = 1
        for i in s:
            if i[0] == a and i[1] == 'язык программирования':
                print(f'{a} был создан: {i[3]} в {i[2]}')
                f = 0
                break
        if f:
            print('Хм.. Вы уверены, что слышали об этом ЯП?')