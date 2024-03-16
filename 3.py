import csv
with open("languages.csv", encoding='utf8') as r:
    s = csv.reader(r, delimiter=';', quotechar='"')
    s = list(s)
    del s[0]
    v = []  # Список кортежей языков программирования: (Title, cretors, appeared)
    for i in s:
        if i[1] == 'язык программирования':
            v.append((i[0], i[3], i[2]))
    v = sorted(v)  # сортировка по навзанию ЯП для осуществления двоичного поиска
    while True:
        a = input()  # запрос на введение названия ЯП
        if a == '0':
            break
        f = 1
        left = 0
        right = len(v) - 1
        m = right // 2
        ''' left и right - правая и левая граница двоичного поиска, m = середина'''
        while True:  # двоичный поиск
            if right - left <= 1:
                if v[right][0] == a:
                    print(f'{a} был создан: {v[right][1]} в {v[right][2]}')
                    break
                if v[left][0] == a:
                    print(f'{a} был создан: {v[right][1]} в {v[right][2]}')
                    break
                print('Хм.. Вы уверены, что слышали об этом ЯП?')
                break
            if v[m][0] <= a:
                left = m
                m = (left + right) // 2
            else:
                right = m
                m = (left + right) // 2