import os

print('\nDostepne pliki:')
for file in os.listdir('Z:/emmegifdd/ETX/'):
    if file.endswith(".txt"):
        print(file[:len(file)-4])

while True:
    plik = input('\nWybierz plik z listy: ')
    fileetx = open('Z:/emmegifdd/ETX/' + plik + '.txt', 'r').read()
    lines = fileetx.split('\n')
    print(str(len(lines)/5))