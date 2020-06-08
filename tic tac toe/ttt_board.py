#plik rysujacy plansze, board size wczytujemy z pliku game, poki co zrobiony na stale 3
def dots(board_size):  #funkcja do rysowania kropek czyli poziomej poprzeczki planszy
 print(" ---" * board_size)

def pipes(board_size, piece, j): #rysujemy pionowe slupki planszy
 for i in range(board_size):
  print("|", piece[j][i], end=" "); 
 print ("|")
 
def board_main(piece, size): #rysujemy, piece jest macieza przechowujaca informacje ktore pola maja pusty znak ktore X a ktore O.
 for j in range(size):
  dots(size)
  pipes(size, piece, j)
 dots(size)
 print("\n")

if __name__ == "__main__":  #to zdaje sie jest warunek przez ktory nie uruchomimy board_main przy imporcie board.py. Sprawdzamy czy wywolalismy ten plik, jesli nie to nie ma egzekucji. 
 board_main()