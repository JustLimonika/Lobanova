import csv  #
with open("C:\\Users\\Kids01\\Desktop\\Лобанова Софья Алексеевна школа 1518\\pythonProject1\\languages.csv",
          encoding='utf8') as r:
    s = csv.reader(r, delimiter=';', quotechar='"')
    s = list(s)
    del s[0]
    a = []  # список из названия языка и его рейтинга
    for i in s:
        r = int(i[4]) / (2023 - int(i[2]))
        a.append((i[0], r))
    print(a)