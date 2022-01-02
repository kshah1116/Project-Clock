from tkinter import *
from time import strftime


def tym():
    t= strftime("%H:%M:%S %p")
    lbl.config(text=t)
    lbl.pack()
    #displays the time after certain seconds
    lbl.after(1000,tym)
    

clock=Tk()
clock.title("Clock")
clock.geometry("500x300")
clock.config(bg='black')
clock.resizable(False, False)

#creating Label
lbl= Label(clock,bg="black",fg="red",height="5",font= ('Pompadour Numerals',50,'bold'))
#calling Function
tym()
clock.mainloop()

