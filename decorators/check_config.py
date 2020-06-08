import os
import time
from string import find
from string import join

os.system('cls')

lista_plikow = []
lista_katalogow = []
pliki_xml = []
found = []


class timer:
    def __init__(self, func):
        self.func = func
        self.alltime=0

    def __call__(self, *args):
        start = time.clock()
        result = self.func(*args)
        elapsed = time.clock() - start
        self.alltime += elapsed
        print ('%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime))
        return result


@timer
def list_to_xml(lista_plikow):
    for nazwa_pliku in lista_plikow:
        for i in range(len(nazwa_pliku) - 3):
            if nazwa_pliku[i:i + 4] == '.xml':
                pliki_xml.append(nazwa_pliku)
    return pliki_xml

@timer
def print_dir():
    os.chdir('C:\Checkouts\Wroclaw')
    print(os.getcwd())
    for root, dirs, files in os.walk(".", topdown=False):
       for name in files:
          # print(os.path.join(root, name))
          lista_plikow.append(os.path.join(root, name))
       for name in dirs:
          # print(os.path.join(root, name))
            lista_katalogow.append(os.path.join(root, name))
    return lista_katalogow, lista_plikow

@timer
def find_pattern(pattern, pliki_xml):
    for plik in pliki_xml:
        f = open(plik, 'r')
        lista = f.readlines()
        f.close()
        tekst = join(lista, "")
        szukam = find(tekst, pattern)
        if szukam > -1:
            found.append(plik)
    if len(found) == 0: found.append('nie znaleziono')
    return found


def main():
    lista_katalogow, lista_plikow = print_dir()
    pliki_xml = list_to_xml(lista_plikow)
    znalezione = find_pattern('UHGA', pliki_xml)
    print('\n'.join(znalezione))

main()