import pdb
import os
import numpy
from ttt_UI import *
from ttt_winner import *
from ttt_board import *

def main():
 os.system("cls")
 print ("\n***********************\nWitaj w Tic Tac Toe!!\nGramy do trzech wygranych\n***********************")
 score=[0,0]  #wynik, pierwszy 0,0
 Player = 1   #numer playera, na poczatek pierwszy
 piece = 'X'  #jaki znak wstawiamy, jako pierwszy X
 empty_mark = ' '  #poczatkowo pola wypelniamy pustym znakiem spacji
 size=3 #sprawdzanie wygrywania dziala tylko na rozmiar 3 poki co
 
 while True:  #gramy dopoki nie przerwiemy petli brakiem, ten serszy while pilnuje bysmy mogli grac po wygranej do 3 jeszcze raz. zawiera pytanie czy chcemy jeszcze grac.
  #initial board values
  game = [[empty_mark]*size for i in range(size)]   #game - maciez znakow (wypelnienia) na poczatku mamy puste znaki a potem sukcesywnie wymieniamy puste na konkretne znaki. Pierwsze wywolanie to same puste.
  #initial_board draw
  print("\n\nRuch Player ",Player," --> ",piece)
  board_main(game, size)  #wywolanie funkcji board_main z board.py
   
  while not game_over(game, empty_mark):   #  petla ciagla przerywamy przez break w momencie uzyskania spelninia warunku wygrania. game over sprawdza tylko czy plansza jest pelna
 #  os.system("cls")
   wPlayer=Player #we put here Player to wPlayer(winner player) to remember which player has won
   Player, piece, game=zgaduj(Player, game, piece, empty_mark)   
   
   board_main(game, size)
   if Player==0: score[0]=3; break; #ustawiamy player 0 jesli wcisnieto q podczas zgadywania oznaczajace ze chcemy wyjsc z gry
    
   if winner_main(game, empty_mark): #sprawdzamy czy ktos wygral funkcja z winner.py, jesli tak zwiekszamy wynik i przerywamy petle while
    score[wPlayer-1]=score[wPlayer-1]+1  #jesli tak zwieksz wyniki ogolny meczu
    break  
  print ("wynik:\n Player 1:", score[0],"\n Player 2:",score[1],"\n")   
 # pdb.set_trace()
  
  if score[0] >= 3 or score[1] >= 3:
   print("Game Over")
   
#   pdb.set_trace()
   if input("Do you want to play again? y/n: ")=="y":  #jesli gra sie skonczyla i odpowiedzielismy tak to gramy znowu i zerujemy podstawowe parametry.
    print ("\n*********************\nWitaj w Tic Tac Toe!!\n*********************\n")
    score=[0,0]
    Player = 1
    piece = 'X' 
   else:
    break

	
main()