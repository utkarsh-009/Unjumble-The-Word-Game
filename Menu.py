from tkinter import *

# MENU WINDOW

window = Tk()
window.title('UnJumble The Word Game')

window.state('zoomed')

bg = PhotoImage(file="image/Home.png")


my_label = Label(window, image = bg)
my_label.place( x = 0 ,  y = 0, relwidth=1, relheight= 1)

def switch():
    window.destroy()    

button1 = Button(window, text="Start", font=('Arial', 20), padx= 50, command= switch).place(x = 670, y = 520)

window.mainloop()
