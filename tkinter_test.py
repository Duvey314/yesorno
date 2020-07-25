
#search for outside clicks and check for bots


from tkinter import *

import datetime

import requests

import json

import pandas as pd

import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import functools

#past_data_df = pd.read_csv('data.csv', index_col=0)
#print(past_data_df)

# create the window object
window = Tk()

# size the window
window.geometry('600x550')

# add title to the top bar
window.title("Please Select YES or NO")

# create the label in the window
lbl = Label(window, text="Please Select YES or NO", font=("Arial Bold", 20))
lbl.place(relx = .5, rely = .3, anchor = 'center')


def clicked(event, choice):

    #creates new window for the answer
    answer_window = Toplevel(window) 
    answer_window.title("Answer Window") 
    answer_window.geometry("800x800")
    scrollbar = Scrollbar(answer_window)
    scrollbar.pack(side=RIGHT, fill=Y)
  
    # answer of button press 
    global click
    answer = choice
    ans_lbl = Label(answer_window, text =f"The {answer} button was clicked.")
    ans_lbl.pack(side = TOP)

    # date of button press
    global date
    date = datetime.datetime.now().date()
    date_lbl = Label(answer_window, text = f'The button was pressed on {date}')
    date_lbl.pack(side = TOP)

    # time of button press
    global time
    time = datetime.datetime.now().time()
    time_lbl = Label(answer_window, text = f'The button was pressed at {time}')
    time_lbl.pack(side = TOP)

    # use ip-api to get ip address and location data
    try:
        #get ip adress info
        ip_info = requests.get("http://ip-api.com/json/?fields=query,status,message,country,continent,regionName,city,timezone,isp,mobile,proxy").json()
        ip_address = ip_info['query']
        continent = ip_info['continent']
        country = ip_info['country']
        region = ip_info['regionName']
        city = ip_info['city']
        time_zone = ip_info['timezone']
        isp = ip_info['isp']
        mobile = ip_info['mobile']
        proxy = ip_info['proxy']

    except:
        # if error make null
        ip_address = 'null'
        continent = 'null'
        country = 'null'
        region = 'null'
        city = 'null'
        time_zone = 'null'
        isp = 'null'
        mobile = 'null'
        proxy = 'null'

    # add ip adress label    
    ip_address_lbl = Label(answer_window, text = f"The IP address is {ip_address}.")
    ip_address_lbl.pack(side = TOP)

    # add where on button was pressed
    x, y = event.x, (120-event.y)
    pos_lbl = Label(answer_window, text = f'The mouse was clicked at {x},{y}')
    pos_lbl.pack(side = TOP)
    last_clicked_location = {'x':x,'y':y}
    #new_click_locations_df = click_locations_df.append(last_clicked_location,ignore_index=True)
    #print(new_click_locations_df)

    values = {'ip_address':ip_address,
            'continent':continent,
            'country':country,
            'region':region,
            'city':city,
            'time_zone':time_zone,
            'isp':isp,
            'mobile':mobile,
            'proxy':proxy,
            'answer': answer,
            'date': date,
            'time': time,
            'x':x,
            'y':y}
    
    columns = ['ip_address','continent','country','region','city','time_zone','isp','mobile','proxy','answer','date','time','x','y']

    values_df = pd.DataFrame([values], columns = columns)
    with open('data.csv', 'a', newline='') as f:
        values_df.to_csv(f, header=False, index = False)
    
    answers_df = pd.read_csv('data.csv')  
    yes_answers_df = answers_df[answers_df['answer'] == 'yes']
    no_answers_df = answers_df[answers_df['answer'] == 'no']

    #plot the button press locations
    figure = plt.Figure(figsize=(2.5,1.5), dpi=100)
    ax = figure.add_subplot(111)
    ax.scatter(answers_df['x'],answers_df['y'])
    ax.scatter(x,y,color='red')
    ax.set_xlim(0,200)
    ax.set_ylim(0,120)
    scatter = FigureCanvasTkAgg(figure, answer_window) 
    scatter.get_tk_widget().pack()

    #plot the button press locations for both answers
    figure = plt.Figure(figsize=(2.5,1.5), dpi=100)
    ax = figure.add_subplot(111)
    ax.scatter(yes_answers_df['x'],yes_answers_df['y'],color = 'green')
    ax.scatter(no_answers_df['x'], no_answers_df['y'],color = 'red')
    ax.scatter(x,y,color='blue')
    ax.set_xlim(0,200)
    ax.set_ylim(0,120)
    scatter = FigureCanvasTkAgg(figure, answer_window) 
    scatter.get_tk_widget().pack()

    #plot the answers in a pie
    figure = plt.Figure(figsize=(2,2), dpi=100)
    ax = figure.add_subplot(111)
    ax.pie(answers_df['answer'].value_counts(), autopct ='% 1.1f %%')
    answer_pie = FigureCanvasTkAgg(figure, answer_window) 
    answer_pie.get_tk_widget().pack()
     
    
# add the YES button
yes_btn = Button(window, text="YES", font=("Arial Bold", 40))
yes_btn.place(relx = .25, rely = .66, height = 120, width = 200, anchor = 'center')
yes_btn.bind("<Button-1>", functools.partial(clicked, choice='yes'))

# add the NO button
no_btn = Button(window, text="NO", font=("Arial Bold", 40))
no_btn.place(relx = .75, rely=.66, height = 120, width = 200, anchor = 'center')
no_btn.bind("<Button-1>", functools.partial(clicked, choice='no'))

# keep window open until user input
window.mainloop()