miasta = {'Dublin': 1500000, 'Moskwa': 12000000, 'Wiedeń': 3500000, 'Budapeszt': 200000}

file = open("C:/Dokumenty/miasta.txt", "w", encoding="utf-8")

for miasto, mieszkancy in miasta.items():
    file.write(miasto + ' ' + str(mieszkancy) + '\n')

file.close