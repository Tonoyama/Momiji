#!/usr/bin/python3
import sys, os
from tkinter import *
import tkinter
from tkinter import ttk
from PIL import Image, ImageTk
from fir_win import sub_window0
from fir_win import sub_window1
from fir_win import tk_dialog_csv_0
from fir_win import tk_dialog_csv_1
from fir_win import tk_dialog_csv_2
from fir_win import tk_dialog_csv_3
from fir_win import sub_win_visu0
from fir_win import tk_dialog_csv_5
from fir_win import tk_dialog_csv_6
from fir_win import tk_dialog_csv_7
from fir_win import tk_dialog_csv_8
from fir_win import tk_dialog_csv_9
from fir_win import txt_0
from fir_win import txt_1
from fir_win import txt_2
from fir_win import txt_3
from fir_win import txt_4
from fir_win import txt_5
from fir_win import auto_0

#logo icon
if __name__ == "__main__":
    root = Tk()

#Image
image_0 = Image.open("./Momiji_linux/pic/wide_data_lineplot.png")
image = ImageTk.PhotoImage(image_0)
canvas = tkinter.Canvas(bg="#f3f9fb",width=1920, height=1080)
canvas.place(x=0, y=0)
canvas.create_image(5, 210, image=image, anchor=tkinter.NW)

image_1 = Image.open(r"./Momiji_linux/pic/grouped_violinplots.png")
image_1 = ImageTk.PhotoImage(image_1)
canvas.create_image(210, 210, image=image_1, anchor=tkinter.NW)

image_2 = Image.open(r"./Momiji_linux/pic/joint_kde.png")
image_2 = ImageTk.PhotoImage(image_2)
canvas.create_image(415, 210, image=image_2, anchor=tkinter.NW)

image_3 = Image.open(r"./Momiji_linux/pic/heatmap_annotation.png")
image_3 = ImageTk.PhotoImage(image_3)
canvas.create_image(620, 210, image=image_3, anchor=tkinter.NW)

#Data creaning
def button0():
    tk_dialog_csv_0.file_search()
def button1():
    tk_dialog_csv_1.file_search()
def button2():
    tk_dialog_csv_2.file_search()
def button3():
    tk_dialog_csv_3.file_search()

#Data Visualization
def button4():
    sub_win_visu0.sub_window0()
def button5():
    tk_dialog_csv_5.file_search()
def button6():
    txt_2.file_search()
def button7():
    tk_dialog_csv_7.file_search()
def button8():
    tk_dialog_csv_8.file_search()
def button9():
    tk_dialog_csv_9.file_search()

#Natural Language Processing
def button_nlp_0():
    txt_0.process()
def button_nlp_1():
    txt_1.file_search()
def button_nlp_2():
    txt_0.process()
def button_nlp_3():
    txt_0.process()
def button_nlp_4():
    txt_0.process()
def button_nlp_5():
    txt_0.process()

#automatic
def automatic_0():
    auto_0.auto()

#sub_window
def sub_win0():
    sub_window0.sub_window()
def sub_win1():
    sub_window1.sub_window()

#quit
def quit():
    root.quit()

#Label
label_0 = ttk.Label(text=u'Data creaning[.csv]',background='#f3f9fb')
label_0.place(x=5, y=5)
label_1 = ttk.Label(text=u'Data Visualization[.csv]',background='#f3f9fb')
label_1.place(x=5, y=150)
label_2 = ttk.Label(text=u'Natural Language Processing[.txt]',background='#f3f9fb')
label_2.place(x=400, y=5)

root.title("Momiji")
root.configure(width = 850, height=600,background='#f3f9fb')

#Data creaning
button0 = ttk.Button(text=u"Delete duplicate rows",width=25,command=button0)
button0.place(x=5, y=30)

button1 = ttk.Button(text=u"Fill blanks with avg.",width=25,command=button1)
button1.place(x=195, y=30)

button2 = ttk.Button(text=u"Delete duplicate rows",width=25,command=button2)
button2.place(x=5, y=60)

button3 = ttk.Button(text=u"Delete duplicate rows",width=25,command=button3)
button3.place(x=195, y=60)

#Data Visualization
button4 = ttk.Button(text=u"Line plot",width=27,command=sub_win_visu0)
button4.place(x=5, y=180)

button5 = ttk.Button(text=u"Violin plot",width=27,command=button5)
button5.place(x=210, y=180)

button6 = ttk.Button(text=u"Joint KDE",width=27,command=button6)
button6.place(x=415, y=180)

button7 = ttk.Button(text=u"Heat map",width=27,command=button7)
button7.place(x=620, y=180)

button8 = ttk.Button(text=u"Random Forest",width=27,command=button8)
button8.place(x=5, y=420)

button9 = ttk.Button(text=u"LightGBM",width=27,command=button9)
button9.place(x=210, y=420)

#Natural Language Processing
button_nlp_0 = ttk.Button(text=u"Lowercase",width=25,command=button_nlp_0)
button_nlp_0.place(x=400, y=30)

button_nlp_1 = ttk.Button(text=u"Delete HTML Tag",width=25,command=button_nlp_1)
button_nlp_1.place(x=590, y=30)

button_nlp_2 = ttk.Button(text=u"Delete duplicate rows",width=25,command=button_nlp_2)
button_nlp_2.place(x=400, y=60)

button_nlp_3 = ttk.Button(text=u"Delete duplicate rows",width=25,command=button_nlp_3)
button_nlp_3.place(x=590, y=60)

button_nlp_4 = ttk.Button(text=u"Delete duplicate rows",width=25,command=button_nlp_4)
button_nlp_4.place(x=400, y=90)

button_nlp_5 = ttk.Button(text=u"Fill blanks with avg.",width=25,command=button_nlp_5)
button_nlp_5.place(x=590, y=90)

#automatic funcion
automatic_0 = ttk.Button(text=u'Automatic',width=52,command=automatic_0)
automatic_0.place(x=5 , y=90)

#sub_window
sub_button0 = ttk.Button(text=u'More function',width=52,command=sub_win0)
sub_button0.place(x=5 , y=120)

sub_button1 = ttk.Button(text=u'More function',width=56,command=sub_win1)
sub_button1.place(x=5 , y=500)

sub_button3 = ttk.Button(text=u'More function',width=52,command=sub_win0)
sub_button3.place(x=400 , y=120)

#Quit
button_q = ttk.Button(text=u'Quit',width=100,command=quit)
button_q.place(x=5, y=560)

root.mainloop()
