#Draw hangman
import os

def draw_hangman():
 draw=[]
 draw.append('        /___\\')
 draw.append('         / \ ')
 draw.append('          |')
 draw.append('   ________')
 draw.append('   |      |')
 draw.append('   O      |\n / | \    |\n  / \     |')
 
 steps=[]
 steps.append(draw[0])
 steps.append(draw[1]+"\n"+draw[0])
 steps.append(("\n"+draw[2])*6+"\n"+draw[1]+"\n"+draw[0]) 
 steps.append(draw[3]+"\n"+draw[2]+("\n"+draw[2])*5+"\n"+draw[1]+"\n"+draw[0]) 
 steps.append(draw[3]+"\n"+draw[4]+"\n"+draw[2]+("\n"+draw[2])*4+"\n"+draw[1]+"\n"+draw[0])  
 steps.append(draw[3]+"\n"+draw[4]+"\n"+draw[5]+"\n"+draw[2]+"\n"+draw[2]*1+"\n"+draw[1]+"\n"+draw[0]) 
 return steps 
 
 
 """
 
 draw.append('        /___\\')
 
 draw.append('         / \ ')
 
 draw.append('          |')
 
 draw.append('   ________')
 
 draw.append('   |      |')
 
 draw.append('   O      |\n / | \    |\n  / \     |')
 
 
 os.system("cls")
 print(draw[0])
 f=input('')
 os.system("cls")
 print(draw[1]+"\n"+draw[0])
 f=input('')
 os.system("cls")
 print(("\n"+draw[2])*6+"\n"+draw[1]+"\n"+draw[0]) 
 f=input('')
 os.system("cls")
 print(draw[3]+"\n"+draw[2]+("\n"+draw[2])*5+"\n"+draw[1]+"\n"+draw[0]) 
 f=input('')
 os.system("cls") 
 print(draw[3]+"\n"+draw[4]+"\n"+draw[2]+("\n"+draw[2])*4+"\n"+draw[1]+"\n"+draw[0])  
 f=input('')
 os.system("cls") 
 print(draw[3]+"\n"+draw[4]+"\n"+draw[5]+"\n"+draw[2]+"\n"+draw[2]*1+"\n"+draw[1]+"\n"+draw[0])    
"""

draw_hangman()