# 3 Customised Dices, One woth more Chancrs to print 6, other with 3 and third with number 1

from tkinter import*
from PIL import ImageTk, Image  
import random

window = Tk()
window.title("Dice Simulator")
window.geometry("920x333") 
window.maxsize(920,333)  
window.minsize(920,333)                              # window size width x height

f1 = Frame(window,highlightcolor= "lightgreen")
f1.pack( side= LEFT, pady= 5, padx= 25)
f2 = Frame(window,highlightcolor= "lightgreen")
f2.pack( side= LEFT, pady= 5, padx= 15)
f3 = Frame(window,highlightcolor= "lightgreen")
f3.pack( side= LEFT, pady= 5, padx= 15)

Heading1 = Label(f1, text="Dice Simulator with more probability of 6",
   fg = "light green",  bg = "dark blue", font = "Helvetica 10 bold")
Heading1.pack() 

Heading2 = Label(f2, text="Dice Simulator with more probability of 3",
   fg = "light green",  bg = "dark blue", font = "Helvetica 10 bold")
Heading2.pack() 

Heading3 = Label(f3, text="Dice Simulator with more probability of 1",
   fg = "light green",  bg = "dark blue", font = "Helvetica 10 bold")
Heading3.pack() 

def random_img():
                   # more Chances of 6
       Dice1 = ['1f.png', '2f.png','3f.png','4f.png','5f.png','6f.png','6f.png','6f.png']
       photo1 = ImageTk.PhotoImage(Image.open(random.choice(Dice1)))
       label1.configure(image=photo1)
       label1.image = photo1              # keep a reference

                   # More Chances of 3
       Dice2 = ['1f.png','2f.png','3f.png','3f.png','3f.png','4f.png','5f.png','6f.png']
       photo2 = ImageTk.PhotoImage(Image.open(random.choice(Dice2)))
       label2.configure(image=photo2)
       label2.image = photo2 

                   # More Chances of 1
       Dice3 = ['1f.png','2f.png','3f.png','4f.png','5f.png','6f.png','1f.png','1f.png']
       photo3 = ImageTk.PhotoImage(Image.open(random.choice(Dice3)))
       label3.configure(image=photo3)
       label3.image = photo3     
       
label1 = Label(f1, height=160, width=160)
label2 = Label(f2, height=160, width=160)
label3 = Label(f3, height=160, width=160)
random_img()
label1.pack(pady= 10)
label2.pack(pady= 10)
label3.pack(pady= 10)
btn = Button(window,  fg= "red", font = "Helvetica 20 bold",text = "click me", command= random_img, 
background='yellow', highlightcolor='green', highlightthickness=0)
btn.place(x=200, y=270)
btn.config(width=30)

window.mainloop()    