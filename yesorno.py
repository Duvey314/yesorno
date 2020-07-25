from tkinter import *

import datetime

import requests

import json

import pandas as pd

import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import functools

# https://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html

class choice_window:
    '''
This is a descriptor
    '''
    def __init__(self,master):
        # set master as the master window
        self.master = master
        master.title = ('Please Make a Selection')
        master.geometry('600x550')

        self.label = Label(master,  text="Please Select YES or NO", font=("Arial Bold", 20))
        self.label.place(relx = .5, rely = .3, anchor = 'center')

        self.yes_btn = Button(master, text="YES", font=("Arial Bold", 40))
        self.yes_btn.place(relx = .25, rely = .66, height = 120, width = 200, anchor = 'center')
        #self.yes_btn.bind("<Button-1>", functools.partial(self.result, choice ='yes'))
        
        # add the NO button
        self.no_btn = Button(master, text="NO", font=("Arial Bold", 40))
        self.no_btn.place(relx = .75, rely=.66, height = 120, width = 200, anchor = 'center')
        #self.no_btn.bind("<Button-1>", functools.partial(answer_window.results, choice ='no'))

class answer_window:
    '''
This is a descriptor
    '''
    def __init__(self):
        # set master as the master window
        Toplevel.__init__(self)
        self.title = ('Please Make a Selection')
        self.geometry('600x550')
    
    def results (event, choice):
        # Get the button pressed
        decision = choice
        ans_lbl = Label(answer, text =f"The {decision} button was clicked.")
        ans_lbl.grid(column = 0, row = 0)

        

        

root = Tk()
yesorno = choice_window(root)
root.mainloop()