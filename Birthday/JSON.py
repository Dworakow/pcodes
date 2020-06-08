#JSON birthday
import json
from collections import Counter


def zlicz_m():
 num_to_string = {
	1: "January",
	2: "February",
	3: "March", 
	4: "April",
	5: "May",
	6: "June",
	7: "July",
	8: "August",
	9: "September",
	10: "October",
	11: "November",
	12: "December"
 }

 list=[]
 dict={}
 months=[]
#print(dict)
 with open ("baza_urodzin.json", 'r') as jw:
  dict=json.load(jw)
 #print(dict)
 for x in dict.values():
  list.append(x)
#print(list)

 for x in range(len(list)):
  #print(list[x][3:5])
  months.append(int(list[x][3:5]))
 
 msc=Counter(months)
#print(months)
 print(msc)

 for x in msc:
  print(x,": {}" .format(msc[x]))
 return msc
 
if __name__ == "__main__":
 zlicz_m()