from tkinter import *

import datetime

import requests

import json

# ip_info = requests.get("http://ip-api.com/json/?fields=query,status,message,continent,country,region,regionName,city,district,zip,lat,lon,timezone,isp,org,as,reverse,mob")
# ip_info_json = ip_info.json()
# print(ip_info_json)
    



# create the window object
window = Tk()

# size the window
window.geometry('600x550')

# add title to the top bar
window.title("Please Select YES or NO")

# create the label in the window
lbl = Label(window, text="Please Select YES or NO", font=("Arial Bold", 20))
lbl.grid(column=0, row=0)


def clickedYES():

    global click
    answer = 'yes'
    
    answer_window = Toplevel(window) 
  
    # sets the title of the 
    # Toplevel widget 
    answer_window.title("Answer Window") 
  
    # sets the geometry of toplevel 
    answer_window.geometry("600x550") 
  
    # A Label widget to show in toplevel 
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
    

# add the YES button
btn = Button(window, text="YES", command = clickedYES)
btn.grid(column=0, row=9)

def clickedNO():

    answer_window = Toplevel(window) 
  
    # sets the title of the 
    # Toplevel widget 
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

    



# add the NO button
btn = Button(window, text="NO", command = clickedNO)
btn.grid(column=1, row=9)

# keep window open until user input
window.mainloop()