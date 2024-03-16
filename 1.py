import csv
with open("C:\\Users\\Kids01\\Desktop\\Лобанова Софья Алексеевна школа 1518\\pythonProject1\\languages.csv",
          encoding='utf8') as r, open("count_book.txt", 'w') as w:
    s = csv.reader(r, delimiter=';', quotechar='"')
    s = list(s)
    del s[0]
    d = dict()  # словарь: ключ - название тем, значение - колмичество книг по этой теме
    for i in s:
        a = i[1]
        b = int(i[4])
        if a in d:
            d[a] += b
        else:
            d[a] = b
    for i in d.keys():
        print(f'Книг для изучения {i} в библиотеке нашлось: {d[i]}', file=w)
    a = input()
    print(f'Для изучения этой темы можно воспользоваться {d[a]} книгами')
