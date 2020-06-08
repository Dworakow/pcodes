import numpy
import pdb

def row_win(game, empty_mark): # warunek wygrania w linii
 for i in range(3):
  if len(set(game[i]))==1 and empty_mark not in set(game[i]):
   r_winner = set(game[i])
   return r_winner
 return 0
 
def col_win(game, empty_mark): #warunek wygrania w pionie
 trans = numpy.transpose(game)
 #pdb.set_trace()
 for i in range(3):
  if len(set(trans[i]))==1 and empty_mark not in set(trans[i]):
   c_winner = set(trans[i])
   return c_winner
 return 0
 
def diag_win(game, empty_mark): #warunek wygrania po skosie
 #1 skos
 if game[0][0] == game[1][1] == game[2][2] and empty_mark not in game[1][1]:
  d_winner=game[1][1]
  return d_winner
 
 #2 skos
 if game[0][2] == game[1][1] == game[2][0] and empty_mark not in game[1][1]:
  d_winner=game[1][1]
  return d_winner
 return 0

def winner_main(game, empty_mark): #musimy podac tu jaki jest pusty znak by moc stwierdzic ze znaki w lini sa takie same ale to nie jest pusty znak.
 #sprawdzanie warunkow
 c_winner=col_win(game, empty_mark)
 r_winner=row_win(game, empty_mark)
 d_winner=diag_win(game, empty_mark)
 
 #jesli ktoras ze zmiennych (moze byc wiecej jak jedna) jest rozna od zero to mamy zwyciezce o znaku jak podano
 #sprawdzamy po kolei
 #jesli warunek spelniony to glowna funkcja zwraca 1 jesli nie to zero.
 if c_winner!=0: print("Columns, Player "+ str(c_winner) + " wins"); return 1
 elif r_winner!=0: print("Rows, Player "+ str(r_winner) + " wins"); return 1
 elif d_winner!=0: print("Diagonals, Player "+ str(d_winner) + " wins"); return 1
 return 0

 
if __name__ == "__main__":
 winner_main()
