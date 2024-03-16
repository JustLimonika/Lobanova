import csv  #
with open("C:\\Users\\Kids01\\Desktop\\Вариант 18\\languages.csv",
          encoding='utf8') as r:
    s = csv.reader(r, delimiter=';', quotechar='"')
    s = list(s)
    del s[0]
    a = dict()  # словарь: ключ - название ЯП, значение - строкка с информацией о нем
    for i in s:
        a[i[0]] = ', '.join(i[1::])
    print(a)