import tkinter
from tkinter import *
from PIL import ImageTk, Image
import os 
import tkinter.messagebox
import random

top =tkinter.Tk() # For Python3.0 --> top = tkinter.tk()
top.title("Rock | Paper | Scissor| Pencil")
user_score = 0
comp_score = 0
def Rock():
    global user_score, comp_score
    
    comp = random.randint(1,4)
    #print("your choice: Rock")
    #print("Comp choice: "+str(comp))
    if comp == 3:
        comp = "Scissor"
        user_score+=1
        tkinter.messagebox.showinfo("Congratulation!!", "YOU WIN!!\n"+"Your Choice:Rock"+"\nComp Choice: "+comp+"\n Rock hits the scissor \nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
        
    elif comp == 4:
        comp = "Pencil"
        user_score+=1
        tkinter.messagebox.showinfo("Congratulation!!", "YOU WIN!!\n"+"Your Choice:Pencil"+"\nComp Choice: "+comp+"\n rock crushes the pencil \nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
        
    elif comp==2:
        comp = "Paper"
        comp_score+=1
        tkinter.messagebox.showinfo("Hard Luck!!", "YOU LOOSE!!\n"+"Your Choice:Rock"+"\nComp Choice: "+comp+"\npaper wraps the rock\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
    
    else :
        comp = "Rock"
        tkinter.messagebox.showinfo("Same pinch!!", "IT'S A TIE!! !!\n"+"Your Choice:Rock"+"\nComp Choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))   
           
    
    
def paper():
    global user_score, comp_score
    
    comp = random.randint(1,4)
    #print("your choice: paper")
    #print("Comp choice: "+str(comp))
    if comp == 1:
        comp = "Rock"
        user_score+=1
        tkinter.messagebox.showinfo("Congratulation!!", "YOU WIN!!\n"+"Your Choice:Paper"+"\nComp Choice: "+comp+"\n paper wraps the rock \nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
   
    elif comp == 4:
        comp = "Pencil"
        comp_score+=1
        tkinter.messagebox.showinfo("Congratulation!!", "YOU Loose!!\n"+"Your Choice:Paper"+"\nComp Choice: "+comp+"\n pencil makes the page dirty\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))

     
    elif comp==3:
        comp = "Scissor"
        comp_score+=1
        tkinter.messagebox.showinfo("Hard Luck!!", "YOU LOOSE!!\n"+"Your Choice:Paper"+"\nComp Choice: "+comp+"\n scissor cuts the paper\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
        
    else :
        comp = "Paper"
        tkinter.messagebox.showinfo("Same pinch!!", "IT'S A TIE!!\n"+"Your Choice:Paper"+"\nComp Choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score)) 
        
def scissor():
    global user_score, comp_score
    
    comp = random.randint(1,4)
    #print("your choice: scissor")
    #print("Comp choice: "+str(comp))
    if comp == 2:
        comp = "Paper"
        user_score+=1
        tkinter.messagebox.showinfo("Congratulation!!", "YOU WIN!!\nYour Choice: Scissor\n"+"Comp choice: "+comp+"\nScissor cuts the paper\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
        
    elif comp==3:
        comp = "Scissor"
        tkinter.messagebox.showinfo("Same pinch!!", "IT'S A TIE!!\nYour Choice: Scissor\n"+"Comp choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score)) 
        
    elif comp == 4:
        comp = "Pencil"
        user_score+=1
        tkinter.messagebox.showinfo("Congratulation!!", "YOU WIN!!\nYour Choice: Scissor\n"+"Comp choice: "+comp+"scissor hits the pencil\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
   
    else:
        comp = "Rock"
        comp_score+=1
        tkinter.messagebox.showinfo("Hard Luck!!", "YOU LOOSE!!\nYour Choice: Scissor\n"+"Comp choice:"+comp+"\nrock hits the scissor\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
        
def pencil():
    global user_score, comp_score
    
    comp = random.randint(1,4)
    #print("your choice: scissor")
    #print("Comp choice: "+str(comp))
    if comp == 2:
        comp = "Paper"
        user_score+=1
        tkinter.messagebox.showinfo("Congratulation!!", "YOU WIN!!\nYour Choice: Pencil\n"+"Comp choice: "+comp+"\n pencil makes the page dirty\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
        
    elif comp==3:
        comp = "Scissor"
        comp_score+=1
        tkinter.messagebox.showinfo("Bad Luck!!", "You LOOSE!!\nYour Choice: Pencil\n"+"Comp choice: "+comp+"\n scissor crashes the pencil\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score)) 

        
    elif comp==1:
        comp = "Rock"
        comp_score+=1
        tkinter.messagebox.showinfo("Hard Luck!!", "YOU LOOSE!!\nYour Choice: Pencil\n"+"Comp choice:"+comp+"\n rock hits the pencil\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
    
    else:
        comp = "Pencil"
        tkinter.messagebox.showinfo("Same pinch!!", "IT'S A TIE!!\nYour Choice: Pencil\n"+"Comp choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score)) 

B1 = tkinter.Button(top, command = Rock)
r = PhotoImage(file = "rock.png")
B1.config(image = r, compound = RIGHT)
r1 = r.subsample(6,6)
B1.config(image = r1)
B2 = tkinter.Button(top, command = paper)
pa = PhotoImage(file = "paper3.png")
B2.config(image = r, compound = RIGHT)
pa1 = pa.subsample(2,3)
B2.config(image = pa1)
B3 = tkinter.Button(top, command = scissor)
s = PhotoImage(file = "sci.png")
B3.config(image = s, compound = RIGHT)
s1 = s.subsample(2,2)
B3.config(image = s1)
B4=  tkinter.Button(top,command=pencil)
pe = PhotoImage(file = "pencil.png")
B4.config(image = pe, compound = RIGHT)
pe1 = pe.subsample(2,2)
B4.config(image = pe1)
B1.pack(side='left')
B2.pack(side='left')
B3.pack(side='left')
B4.pack(side='left')
top.mainloop()
