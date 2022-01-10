import tkinter
from tkinter import *

import random
from tkinter import messagebox
from random import shuffle

from tkinter import *
import Menu

window = Tk()
window.title('UnJumble The Word Game')

window.state('zoomed')

bg = PhotoImage(file="image/bg.png")


my_label = Label(window, image = bg)
my_label.place( x = 0 ,  y = 0, relwidth=1, relheight= 1)

##################  TIMER #######################################
running = False
seconds = 60 #seconds
score = 0

def start():
    global running
    if not running:
        update()
        running = True

def update():
    # update seconds with (addition) compound assignment operator
    global seconds
    seconds = seconds - 1
    if seconds >=0 :
        string_sec = f'{seconds}'
        # update timer label after 1000 ms (1 second)
        stopwatch_label.config(text=string_sec)
        # after each second (1000 milliseconds), call update function
        # use update_time variable to cancel or pause the time using after_cancel
        global update_time
        update_time = stopwatch_label.after(1000, update)
    if seconds == 0:
        total_score = f'{score}'
        messagebox.showinfo("Time's Up!", "Your score is: "  + total_score)


########## UnJumble The Word Game Logic #########
answer = ["license", "true","view","shelter","twig","wish","grip","cricket","ocean","magenta","flowers","ordinary","account","jolly","woman","man","spot","reflect","crowd","limit","jam","marble","bath","funny","look","smart","college","person","jump","birds","wink","mountain","hug","dance","talk","apple"]

words_list = []


for i in answer:
    word = list(i)
    shuffle(word)
    words_list.append(word)

select_random_index = random.randint(0, len(words_list) - 1)

def initial():
    global words_list,select_random_index
    lbl.configure(text= words_list[select_random_index])


def ans_check():
    global words_list, select_random_index, answer, score
    user_input = e1.get()
    if user_input == answer[select_random_index]:
        score = score + 10
        score_board()
        reset()
    else:
        messagebox.showerror("Wrong!", "Your answer is wrong :(")



def reset():
    global words_list, select_random_index, answer
    select_random_index = random.randint(0, len(words_list) - 1)
    lbl.configure(text = words_list[select_random_index])
    e1.delete(0,END)    


def restart():
    
    global running
    if running:
        # cancel updating of time using after_cancel()
        stopwatch_label.after_cancel(update_time)
        running = False
    # pause() 
    global seconds
    seconds = 60
    stopwatch_label.config(text= f'{seconds}')
    reset()
    start()

def score_board():
    score_label = tkinter.Label(text= 'Score: ' + str(score), font=('Arial', 20))
    score_label.place(x= 600, y = 65)


############ Layout #############


top_frame = tkinter.Frame(window).pack(side= 'top')

timer_label = tkinter.Label(text= 'Time: ', font=('Arial', 20))
timer_label.place(x= 1200, y = 65)
stopwatch_label = tkinter.Label(text= '60', font=('Arial', 20))
stopwatch_label.place(x = 1275, y = 67)



lbl = Label(window, font= ("Helvetica" , 50),pady= 20)
lbl.place(x = 600, y = 150)

answer1 = StringVar()
e1 = Entry(window, textvariable= answer, highlightthickness= 2)
e1.config(highlightbackground = "blue", highlightcolor= "blue")
e1.place(x = 600, y = 345, height= 30, width= 300)


button1 = Button(window, text= ("Check" ),font= ("Helvetica" , 15),  command= ans_check)
button1.place(x = 500, y = 420,  height= 35, width= 75)
window.bind('<Return>',lambda event:ans_check())

#########
timer_label = tkinter.Label(text= 'Score: ' + str(score), font=('Arial', 20))
timer_label.place(x= 600, y = 65)
######## 

button2 = Button(window, text= "Restart",font= ("Helvetica" , 15), width= 20, command= restart)
button2.place(x = 900, y = 420,height= 35, width= 75)


initial()
restart()
window.mainloop()
