from tkinter import *
import pandas
import random
timer=None
try:
    data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data=pandas.read_csv(r"C:\Users\ishas\PycharmProjects\day-31\day-31\data\french_words.csv")
data_dict=data.to_dict(orient="records")
current_card={}
# def count_down(count):
#     global timer
#     canvas.itemconfig(time_text, text=count)
#     if count>0:
#         timer=window.after(1000, count_down,count-1)
#     else:
#         flip_card()
def known_card():
    global current_card
    data_dict.remove(current_card)
    d=pandas.DataFrame(data_dict)
    d.to_csv("data/words_to_learn.csv",index=False)
    next_card()


def next_card():
    global current_card,flip_timer
    # if timer:
    #     window.after_cancel(timer)
    window.after_cancel(flip_timer)

    current_card=random.choice(data_dict)
    canvas.itemconfig(card_bg,image=front_card)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    flip_timer=window.after(3000,flip_card)
    # count_down(3)

def flip_card():
    canvas.itemconfig(card_bg,image=card_back)
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")


BACKGROUND_COLOR = "#B1DDC6"
window=Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.title("Flashy")
flip_timer=window.after(3000,flip_card)

front_card=PhotoImage(file=r"C:\Users\ishas\PycharmProjects\day-31\day-31\images\card_front.png")
right_image=PhotoImage(file=r"C:\Users\ishas\PycharmProjects\day-31\day-31\images\right.png")
wrong_image=PhotoImage(file=r"C:\Users\ishas\PycharmProjects\day-31\day-31\images\wrong.png")
card_back=PhotoImage(file=r"C:\Users\ishas\PycharmProjects\day-31\day-31\images\card_back.png")
canvas=Canvas(height=526,width=800,bg=BACKGROUND_COLOR,highlightthickness=0)
card_bg=canvas.create_image(400,263,image=front_card)
card_title=canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)
right_button=Button(image=right_image,command=known_card)
right_button.grid(row=1,column=1)
wrong_button=Button(image=wrong_image,command=next_card)
wrong_button.grid(row=1,column=0)
next_card()
# canvas.grid()




window.mainloop()

