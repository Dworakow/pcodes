#Bithday dictionares
import pdb
import json
import JSON
from bokeh.plotting import figure, show, output_file

def zapis(json_dict):
#zapis do pliku nowej pary imie urodziny
  with open('baza_urodzin.json','w') as write_file:  #zapis do pliku w tym samym katalogu co plik z kodem. Parametr 'a' daje mozliwosc dopisania linii na koncu pliku.
   json.dump(json_dict, write_file)
   write_file.close()
 
def odczyt(): 
 #zaladowanie z pliku json do slownika
 birth_dict={}
 
 with open('baza_urodzin.json','r') as open_file:
  birth_dict=json.load(open_file)   #odczytujemy caly plik i wrzucamy jako string do zmiennej list
 return birth_dict

def wprowadzenie_danych():
 with open('baza_urodzin.json','r') as open_file:
  json_dict=json.load(open_file)
  print(json_dict,'\n')
  open_file.close()
 imie=input("Wprowadz imie: ").title()
 json_dict[imie]=input("Wprowadz date urodzin: ")
 print(json_dict)
 return json_dict 

#wywolanie imienia ze slownika i wyswietlenie formulki z urodzinami
def wywolanie(birth_dict):
 imie=input('Podaj imie dla ktorego chcesz wywolac urodziny: ').title()
 print(birth_dict[imie])   
  
def plot(msc):
 # we specify an HTML file where the output will go
 x=[]
 y=[]
 output_file("plot.html")


# load our x and y data
 for i in msc:
  x.append(i)
  y.append(msc[i])
# create a figure
 p = figure()

# create a histogram
 p.vbar(x=x, top=y, width=0.3)

# render (show) the plot
 show(p)
  
  
def main():
 try:
  if input("Czy chcesz wprowadzic nowe dane do pliku?\nZostana dopisane na koncu pliku. \ny/n:").upper()=="Y":
   zapis(wprowadzenie_danych())
  for x in odczyt():
   print(x)    #wypisujemy wszystkie klucze. Domyslnie w slownikach nie mamy dostepu do wartosci wiec jesli chcemy ko kolei wywietlic slownik to dostaniemy same klucze. Ot taki trik
   
  while True:
   wywolanie(odczyt())


 except KeyError: print("\npodaj imie a nie jakas pierdole !!")
 plot(JSON.zlicz_m())
  
main()