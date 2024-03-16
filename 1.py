import csv
with open("C:\\Users\\Kids01\\Desktop\\Вариант 18\\languages.csv",
          encoding='utf8') as r, open("count_book.txt", 'w') as w:
    s = csv.reader(r, delimiter=';', quotechar='"')
    s = list(s)
    del s[0]
    d = dict()  # словарь: ключ - название тем, значение - колмичество книг по этой теме
    for i in s:
        b = int(i[4])  # количество книг для изучения
        if i[1] in d:
            d[i[1]] += b
        else:
            d[i[1]] = b
    for i in d.keys():
        print(f'Книг для изучения {i} в библиотеке нашлось: {d[i]}', file=w)
    a = input()
    print(f'Для изучения этой темы можно воспользоваться {d[a]} книгами')
