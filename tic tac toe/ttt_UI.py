import pdb
import os

def zgaduj(Player, game, piece, empty_mark): #silnik uzupelniania planszy, podajemy 1,1 wiec musimy rozbic na rzad i kolumne.
 guess=input("Player "+str(Player)+" {"+str(piece)+"} podaj lokalizacje, nr rzedu i kolumny po przecinku np. (1,1):\n")	
 if guess == "q":
  return 0, piece, game
  
 row,col=guess.split(",")
 os.system("cls")
 if game[int(row)-1][int(col)-1]==empty_mark: #check if place is free
  game[int(row)-1][int(col)-1]=piece #put piece in board
  if Player == 1:  #spradzamy ktory player gral i ustawiamy dane tego drugiego
   print("\n\nRuch player 2 --> O")
   Player = 2
   piece = 'O'
  else: 
   print("\n\nRuch player 1 --> X")
   Player = 1
   piece = 'X'
 else: #jesli jest juz wstawiona jakas wartosc to powtarzamy ruch. Tego samego playera
  print("\n******************************************************\nTutaj juz jest wartosc, strzelaj gdzies indziej:\nGra Player "+str(Player)+" {"+str(piece)+"}:\n******************************************************\n")
 return Player, piece, game
 
def game_over(game, empty_mark):  #sprawdzamy czy jest jeszczze miejsce na planszy, jesli tak to zwracamy 0 jesli nie to 1.
	# check if board is full
 for sublist in game:
  if empty_mark in sublist:
   return 0 #still have place
 print ("The board is filled\nIt seems to be draw :)")  
 return 1 #it is full

 """
def UI_main():#tego chyba nie uzywamy ....
	#maciez zer jako pusta plansza
 empty_mark = '-'
 game = [([empty_mark]*3) for i in range(3)]

 Player = 1
 piece = 'X'
 play=True

 while play:
 # pdb.set_trace()
  Player, piece, play, game=zgaduj(play, Player, game, piece, empty_mark)
  if game_over(game, empty_mark)==1: 
    print ("Game over - the board is filled")  
    play=False
    break
"""
if __name__ == "__main__":	
 UI_main()