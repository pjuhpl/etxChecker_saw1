import os, re

iloscetx = 0

print('\nDostępne pliki:')
for file in os.listdir('Z:/emmegifdd/ETX/'):
    if file.endswith(".txt"):
        print(file[:len(file)-4])

while True:
    plik = input('\nWybierz plik z listy: ')
    fileetx = open('Z:/emmegifdd/ETX/' + plik + '.txt', 'r').read()
    lines = fileetx.split('\n')
    iloscetx = 0

    reg = re.compile(r'([0-9]{1,}[.][0-9])([;])([0-9]{1,}[.][0-9])([;])([0-9]{1,}[.][0-9])')
    for i in range(4,len(lines),5):
        try:
            szukaj = reg.search(lines[i])
            szukaj.group()
            iloscetx += 1
        except:
            print('Błąd w okolicy naklejki nr: ' + str(iloscetx+1) + ' (' + str(iloscetx * 5) + ' linia pliku')
            break

    if iloscetx == (len(lines)/5):
        print('Plik z naklejkami jest poprawny.')
        print('Ilość naklejek w pliku: ' + str(iloscetx))
        print('Dla pewności porównaj ilość z listą cięć i sprawdź format naklejki.')