from tkinter import *

import datetime

import requests

import json

import pandas as pd

import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# create the window object
window = Tk()

# size the window
window.geometry('600x550')

# add title to the top bar
window.title("Please Select YES or NO")

# create the label in the window
lbl = Label(window, text="Please Select YES or NO", font=("Arial Bold", 20))
lbl.place(relx = .5, rely = .3, anchor = 'center')

positions = {'x' : [100, 150, 75, 125, 25], 'y':[25, 50, 75, 100, 110]}
click_locations_df = pd.DataFrame(positions, columns = ['x','y'])

def clickedYES(event):

    #creates new window for the answer
    answer_window = Toplevel(window) 
  
    # sets the title of the window
    answer_window.title("Answer Window") 
  
    # sets the size of the answer window 
    answer_window.geometry("600x550") 
  
    # answer of button press 
    global click
    answer = 'yes'
    ans_lbl = Label(answer_window, text =f"The {answer} button was clicked.")
    ans_lbl.grid(column = 0, row = 0)

    # date of button press
    global date
    date = datetime.datetime.now().date()
    date_lbl = Label(answer_window, text = f'The button was pressed on {date}')
    date_lbl.grid(column = 0, row = 1)

    # time of button press
    global time
    time = datetime.datetime.now().time()
    time_lbl = Label(answer_window, text = f'The button was pressed at {time}')
    time_lbl.grid(column = 0, row = 2)

    # use ip-api to get ip address and location data
    try:
        #get ip adress info
        ip_info = requests.get("http://ip-api.com/json/?fields=query,status,message,continent,country,region,regionName,city,district,zip,lat,lon,timezone,isp,org,as,reverse,mob").json()
        ip_address = ip_info['query']
    except:
        # if error make null
        ip_address = 'null'

    # add ip adress label    
    ip_address_lbl = Label(answer_window, text = f"The IP address is {ip_address}.")
    ip_address_lbl.grid(column = 0, row = 3)

    # add where on button was pressed
    x, y = event.x, (120-event.y)
    pos_lbl = Label(answer_window, text = f'The mouse was clicked at {x},{y}')
    pos_lbl.grid(column = 0, row = 4)
    last_clicked_location = {'x':x,'y':y}
    new_click_locations_df = click_locations_df.append(last_clicked_location,ignore_index=True)
    print(new_click_locations_df)

    #plot the button press locations
    figure = plt.Figure(figsize=(5,3), dpi=100)
    ax = figure.add_subplot(111)
    ax.scatter(new_click_locations_df['x'],new_click_locations_df['y'])
    ax.scatter(x,y,color='red')
    ax.set_xlim(0,200)
    ax.set_ylim(0,120)
    scatter = FigureCanvasTkAgg(figure, answer_window) 
    scatter.get_tk_widget().grid(column = 0, row = 5)

def clickedNO(event):

    #create new window for answer
    answer_window = Toplevel(window) 
  
    # sets the title of the window 
    answer_window.title("Answer Window") 
  
    # sets the geometry of toplevel 
    answer_window.geometry("600x550") 
  
    # Get the button pressed
    global answer
    answer = 'no'
    ans_lbl = Label(answer_window, text =f"The {answer} button was clicked.")
    ans_lbl.grid(column = 0, row = 0)
    
    # date of button press
    global date
    date = datetime.datetime.now().date()
    date_lbl = Label(answer_window, text = f'The button was pressed on {date}')
    date_lbl.grid(column = 0, row = 1)

     # time of button press
    global time
    time = datetime.datetime.now().time()
    time_lbl = Label(answer_window, text = f'The button was pressed at {time}')
    time_lbl.grid(column = 0, row = 2)

    # use ip-api to get ip address and location data
    try:
        #get ip address info
        ip_info = requests.get("http://ip-api.com/json/?fields=query,status,message,continent,country,region,regionName,city,district,zip,lat,lon,timezone,isp,org,as,reverse,mob").json()
        ip_address = ip_info['query']
    except:
        # if error make null
        ip_address = 'null'

    # add ip adress label    
    ip_address_lbl = Label(answer_window, text = f"The IP address is {ip_address}.")
    ip_address_lbl.grid(column = 0, row = 3)

    # where on the button was pressed
    x, y = event.x, (120 - event.y)
    pos_lbl = Label(answer_window, text = f'The mouse was clicked at {x},{y}')
    pos_lbl.grid(column = 0, row = 4)
    last_clicked_location = {'x':x,'y':y}
    new_click_locations_df = click_locations_df.append(last_clicked_location,ignore_index=True)
    print(new_click_locations_df)

    #plot the button press locations
    figure = plt.Figure(figsize=(5,3), dpi=100)
    ax = figure.add_subplot(111)
    ax.scatter(new_click_locations_df['x'],new_click_locations_df['y'])
    ax.scatter(x,y,color='red')
    ax.set_xlim(0,200)
    ax.set_ylim(0,120)
    scatter = FigureCanvasTkAgg(figure, answer_window) 
    scatter.get_tk_widget().grid(column = 0, row = 5)
    
# add the YES button
yes_btn = Button(window, text="YES", font=("Arial Bold", 40))
yes_btn.place(relx = .25, rely = .66, height = 120, width = 200, anchor = 'center')
yes_btn.bind("<Button-1>", clickedYES)
yes_btn.bind("<Button-2>", clickedNO)

# add the NO button
no_btn = Button(window, text="NO", font=("Arial Bold", 40))
no_btn.place(relx = .75, rely=.66, height = 120, width = 200, anchor = 'center')
no_btn.bind("<Button-1>", clickedNO)

# keep window open until user input
window.mainloop()