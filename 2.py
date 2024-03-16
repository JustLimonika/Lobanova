import csv


def f(v):  # сортировка пузырьком по типу языков в алфавитном порядке
    for i in range(1, len(v)):
        j = i
        while True:
            if j == 0:
                break
            if v[j][1] >= v[j - 1][1]:
                break
            v[j], v[j - 1] = v[j - 1], v[j]
            j -= 1
    return v  # функция возвращает отсортированный список


with open("languages.csv", encoding='utf8') as r:
    s = csv.reader(r, delimiter=';', quotechar='"')
    s = list(s)
    del s[0]
    s = f(s)
    n = 0
    for i in range(len(s)):
        if n == 3:
            break
        if s[i - 1][1] != s[i][1]:
            print(s[i][1] + ":")
            m = 0
            n += 1
        if m < 3:
            print(f'{s[i][0]} - создатель {s[i][3]}')
            m += 1
