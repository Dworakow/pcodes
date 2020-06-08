#Hangman guessing engine
#for building purpose we will use word EVAPORATE
import os
import pdb
import generator
import draw

#pdb.set_trace()


def pick_letter(word, guess_matrix):
 while True:
  print("\n", ' '.join((str(e) for e in guess_matrix)))
 # print(word)  #jak to odkomentujemy bedziemy widzieli jakie slowo mamy
  letter=input("\nGuess your letter: ")
  letter=letter.upper()
  if letter == '' or letter == " " or letter.isdigit() or len(letter)>1:
   os.system("cls") 
   print("*************************************************************\n")
   print("Wpisales '{0}'! Powtorz wybor!" .format(letter))
  else:
   os.system("cls")   
   print("*************************************************************\n")
   print("Wybrales litere: ",letter); break
 return letter

 #Zaczynamy program
def play_game():
 #deklaracja zmiennych
 word=generator.take_word()
 empty_mark="_"
 guess_matrix= [empty_mark]*len(word)   #tworzymy maciez pustych znakow 
 guess_hist=[] 
 repetition_count = 0
 false_count = 0
 os.system("cls")
 print("\n\n***********Welcome in HANGMAN*************************")
 print("\nSlowo do zgadniecia zawiera {0} liter" .format(len(word)))
 steps=draw.draw_hangman()

 while True:              #dopoki nie przerwiemy petli bedziemy grali
  letter=pick_letter(word, guess_matrix)

 #sprawdzamy czy nie wprowadzamy litery po raz kolejny 
  if letter in guess_hist:
   print("\nLitera juz byla, bedzie kara !!")
   repetition_count = repetition_count+1
  elif letter in word:          #sprawdzamy czy litera jest w slowie
   for x in range(len(word)):  #standardowe przeszukiwanie litera po literze z ifem gdy trafimy litere 
    if word[x]==letter:
     guess_matrix[x]=letter
     print("Brawo trafiles litere!!!")	  
  else:
   print("\nIncorrect!!! Penality!!")
   false_count = false_count+1
#  print("\n", ' '.join((str(e) for e in guess_matrix)))
  guess_hist.append(letter)
  print("\nDotychczasowe proby: ", guess_hist)
 
  if empty_mark not in guess_matrix:    #warunek zakonczenia gry, gdy juz nie ma pustego znaku w maciezy, wtedy przerywamy petle
   print("\n\nZgadles!!! Szukane slowo to {0}!!!" .format(word)) 
   print("Ilosc wszystkich prob {0}" .format(len(guess_hist)))
   print("Ilosc powtornych liter {0}" .format(repetition_count))
   print("Ilosc zlych prob {0}" .format(false_count))
   break
  penality=false_count + repetition_count
  print("Zostalo {0} prob" .format(6-penality))
  if penality > 0: #zabezpieczenie zeby nie wyskoczylo poza zasieg -> -1
   print("\n*****************************\n")
   print(steps[penality-1])
   print("\n*****************************\n")
  if penality > 5 : print("Wisisz! \nKoniec gry\nSzukane slowo to {0}" .format(word));break
  
  
def main_guess():
 
 while True:
  play_game()
  again = input("\n\nDo you want to play again? y/n\n")
  if again != "y":  os.system("cls"); break 


 
  
main_guess()  