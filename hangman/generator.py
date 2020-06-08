import pdb
import random
#Hangman random word generator


def take_word():
 with open('sowpods.txt','r') as w:
  words=list(w)
  chosenone=random.choice(words).split()
  chosenone=' '.join((str(e) for e in chosenone))
  #print(len(words))
  #print(len(chosenone[0]))
  #print(chosenone[0])
 return chosenone

  
if __name__ == "__main__":
 print(take_word())

"""to jest ok ale zauwazylem krotsze i ladniejszy kod
 line=w.readline().strip()
 while line:
  #pdb.set_trace()
  words.append(line)
  n=n+1
  line=w.readline().strip()
print(len(words))
toguess=random.choice(words)
print(toguess)
 
random.shuffle(words)
"""


