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
    return v


with open("C:\\Users\\Kids01\\Desktop\\Лобанова Софья Алексеевна школа 1518\\pythonProject1\\languages.csv",
          encoding='utf8') as r:
    s = csv.reader(r, delimiter=';', quotechar='"')
    s = list(s)
    del s[0] # 'title', 'type', 'appeared', 'creators', 'book_count'
    s = f(s)
    print(s)
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




# 4 2 3 1 5

# 2 4 3 1 5

# 2 3 4 1 5

# 2 3 1 4 5
# 2 1 3 4 5
# 1 2 3 4 5